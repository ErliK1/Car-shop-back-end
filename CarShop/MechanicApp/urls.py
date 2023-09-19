from django.urls import path
from .views import MachinePartCreateView



urlpatterns = [
    path('parts/create/', MachinePartCreateView.as_view(), name='Create the Machine Part'),

]