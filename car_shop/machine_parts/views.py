from django.db import transaction
from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, ListAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from shared.models import Mechanic
from .models import Category, MachinePart
from .serializers import MachineCategories, MachinePartSerializerGeneral, MachinePartCreateSerializer
from shared.permissions import MechanicPermission


# Create your views here.

class CategoriesListCreateView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = MachineCategories

    # def list(self, request, *args, **kwargs):
    #     serializer = MachineCategories(Category.objects.all(), many=True)
    #     data = serializer.data.copy()
    #     for values in data:
    #         if values['image']:
    #             values['image'] = request.build_absolute_uri(Category.objects.get(pk=values['id']).image.url)
    #     return Response(data, status=status.HTTP_200_OK)


class MachinePartsListView(ListAPIView):
    queryset = MachinePart.objects.all()
    serializer_class = MachinePartSerializerGeneral


class CreateMachineView(ListCreateAPIView):
    permission_classes = [IsAuthenticated, MechanicPermission]

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return MachinePartCreateSerializer
        elif self.request.method == 'GET':
            return MachinePartCreateSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            return []
        else:
            return [IsAuthenticated(), MechanicPermission()]

    def get_queryset(self):
        user = self.request.user
        the_queryset = MachinePart.objects.filter(owner__user=user)
        return the_queryset

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        serializer: MachinePartCreateSerializer = self.get_serializer(data=request.data)
        mechanic = Mechanic.objects.get(user=request.user)
        if serializer.is_valid():
            MachinePart.objects.create(owner=mechanic, **serializer.validated_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
