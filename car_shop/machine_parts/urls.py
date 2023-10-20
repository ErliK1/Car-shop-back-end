from django.urls import path

from .views import MachinePartsListView, CategoriesListCreateView, CreateMachineView, MachinePartRetrieveUpdateDestroy

urlpatterns = [
    path('categories/<int:category>/', MachinePartsListView.as_view(), name='Pjeset'),
    path('categories/', CategoriesListCreateView.as_view(), name='Kategorite'),
    path('machineparts/create/', CreateMachineView.as_view(), name='Krijo Nje MachinePart'),
    path('categories/<int:category>/machinepart/<int:pk>/', MachinePartRetrieveUpdateDestroy.as_view(),
         name='Ndrysho, Merr ose Fshi nje Pjese Makine'),


]