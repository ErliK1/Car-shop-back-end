from django.urls import path
from .views import MachinePartListView

urlpatterns = [
    path('list/', MachinePartListView.as_view(), name='Lista e pjeseve'),

]
