from django.shortcuts import render
from rest_framework import status
from rest_framework.renderers import JSONRenderer

from .serializers import MechanicSignUpSerializer
from .models import Mechanic
from django.db import transaction

from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.response import Response


# Create your views here.


class MechanicSignUpView(CreateAPIView):
    queryset = Mechanic.objects.all()
    serializer_class = MechanicSignUpSerializer

    @transaction.atomic
    def post(self, request, *args, **kwargs):
        serializer_var: MechanicSignUpSerializer = self.get_serializer(data=request.data)
        if serializer_var.is_valid():
            sm = serializer_var.save()
            sm_data = MechanicSignUpSerializer(sm)
            return Response(serializer_var.data, status=status.HTTP_201_CREATED)
        return Response(serializer_var.errors, status=status.HTTP_400_BAD_REQUEST)


class MechanicListView(ListAPIView):
    queryset = Mechanic.objects.all()
    serializer_class = MechanicSignUpSerializer
