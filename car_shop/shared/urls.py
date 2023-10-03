from django.urls import path
from .views import MechanicSignUpView, MechanicListView, MechanicChangePasswordView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(),),
    path('signup/', MechanicSignUpView.as_view(), name='The Endpoint for Signing up MEchanic'),
    path('list/', MechanicListView.as_view(), name='Check'),
    path('changepass/', MechanicChangePasswordView.as_view(), name='Change Password')
]