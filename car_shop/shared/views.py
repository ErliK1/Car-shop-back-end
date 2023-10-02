from django.shortcuts import render
from rest_framework import status
from rest_framework.renderers import JSONRenderer

from .serializers import MechanicSignUpSerializer, MechanicChangePasswordSerializer
from .models import Mechanic
from django.db import transaction

from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView
from rest_framework.response import Response
from .permissions import MechanicPermission


# Create your views here.


class MechanicSignUpView(CreateAPIView):
    queryset = Mechanic.objects.all()
    serializer_class = MechanicSignUpSerializer

    @transaction.atomic
    def post(self, request, *args, **kwargs):
        serializer_var: MechanicSignUpSerializer = self.get_serializer(data=request.data)
        if serializer_var.is_valid():
            sm = serializer_var.save()
            return Response(serializer_var.data, status=status.HTTP_201_CREATED)
        return Response(serializer_var.errors, status=status.HTTP_400_BAD_REQUEST)


class MechanicListView(ListAPIView):
    queryset = Mechanic.objects.all()
    serializer_class = MechanicSignUpSerializer

class MechanicChangePasswordView(UpdateAPIView):
    queryset = Mechanic.objects.all()
    serializer_class = MechanicChangePasswordSerializer
    permission_classes = MechanicPermission

    def get_object(self):
        try:
            return Mechanic.objects.get(user=self.request.user)
        except Exception as e:
            return None

    def update(self, request, *args, **kwargs):
        mechanic_serializer = MechanicChangePasswordSerializer(self.get_object(), data=request.data)
        if mechanic_serializer.is_valid():
            data = mechanic_serializer.save()
            if isinstance(data, Mechanic):
                return Response({'message': 'Success'}, status=status.HTTP_202_ACCEPTED)
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
        return Response(mechanic_serializer.errors)


