from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, CreateAPIView

from Shared.models import Mechanic, User
from Shared.serializers import MechanicSerializerLogIn, MechanicSerializerSignUp


# Create your views here.


class GetMechanicInformationAfterLogIn(CreateAPIView):
    queryset = Mechanic.objects.all()
    serializer_class = MechanicSerializerLogIn

    def post(self, request, *args, **kwargs):
        print(request.auth)
        user_set = User.objects.filter(username=request.user.username)
        if user_set.count() == 0:
            return Response({'message': 'USER DNE'}, status=status.HTTP_404_NOT_FOUND)
        user = user_set.first()
        mechanic_for_user = Mechanic.objects.filter(user=user)
        if mechanic_for_user.count() > 0:
            mechanic_serializer_data = self.get_serializer(mechanic_for_user.first()).data
            return Response(mechanic_serializer_data, status=status.HTTP_200_OK)
        return Response({'message': 'USER DNE'}, status=status.HTTP_404_NOT_FOUND)


class MechanicSignUpView(CreateAPIView):
    queryset = Mechanic.objects.all()
    serializer_class = MechanicSerializerSignUp

    def create(self, request, *args, **kwargs):
        mechanic_serializer: MechanicSerializerSignUp = self.get_serializer(data=request.data)
        if mechanic_serializer.is_valid():
            mechanic_serializer.save()
            return Response(mechanic_serializer.validated_data, status=status.HTTP_200_OK)
        return Response(mechanic_serializer.errors, status=status.HTTP_400_BAD_REQUEST)




