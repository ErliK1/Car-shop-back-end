from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Mechanic


class MechanicSignUpSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    username = serializers.CharField(source='user.username')
    email = serializers.EmailField(source='user.email')
    password = serializers.CharField(source='user.password')

    class Meta:
        model = Mechanic
        fields = ['first_name', 'last_name', 'username', 'email', 'password', 'phone_number', 'gender', 'icon']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        password_data = user_data.pop('password')
        user = User(**user_data)
        user.set_password(password_data)
        user.save()
        return Mechanic.objects.create(user=user, **validated_data)