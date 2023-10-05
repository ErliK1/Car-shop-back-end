from django.urls import path

from .views import MachinePartsListView, CategoriesListCreateView

urlpatterns = [
    path('machineparts/<int:category>', MachinePartsListView.as_view(), name='Pjeset'),
    path('categories/', CategoriesListCreateView.as_view(), name='Kategorite'),

]