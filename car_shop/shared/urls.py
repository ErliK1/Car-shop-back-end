from django.urls import path
from .views import MechanicSignUpView, MechanicListView

urlpatterns = [
    path('signup/', MechanicSignUpView.as_view(), name='The Endpoint for Signing up MEchanic'),
    path('list/', MechanicListView.as_view(), name='Check'),
]