from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, ListAPIView
from rest_framework.response import Response

from .models import Category, MachinePart
from .serializers import MachineCategories, MachinePartSerializerGeneral
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


