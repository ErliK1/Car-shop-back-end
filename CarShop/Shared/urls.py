from django.contrib import admin
from django.urls import path
from Shared.views import GetMechanicInformationAfterLogIn, MechanicSignUpView
from rest_framework_simplejwt import views as jwt_views



urlpatterns = [
    path('token-auth/', jwt_views.TokenObtainPairView.as_view(), name='Token Obtain'),
    path('token-refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('login/', GetMechanicInformationAfterLogIn.as_view()),
    path('signup/', MechanicSignUpView.as_view()),
]