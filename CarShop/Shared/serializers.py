from django.db import transaction
from rest_framework import serializers
from .models import User, Mechanic, BigUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class MechanicSerializerLogIn(serializers.ModelSerializer):
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    username = serializers.CharField(source='user.username')
    email = serializers.EmailField(source='user.email')
    gender = serializers.CharField(source='user.gender')
    phone_number = serializers.CharField(source='user.location_address')
    location_address = serializers.CharField(source='user.location_address')
    #user = UserSerializer()

    class Meta:
        model = Mechanic
        fields = ['first_name', 'last_name', 'username', 'email', 'gender', 'phone_number', 'location_address', ]
        # fields = ['user']


class MechanicSerializerSignUp(MechanicSerializerLogIn):
    password = serializers.CharField(source='user.password')

    class Meta(MechanicSerializerLogIn.Meta):
        model = Mechanic
        fields = MechanicSerializerLogIn.Meta.fields + ['password']

    @transaction.atomic
    def create(self, validated_data):
        user_data = validated_data.pop('user')
        password_data = user_data.pop('password')
        user = User(**user_data)
        user.set_password(password_data)
        user.save()
        mechanic = Mechanic.objects.create(user=user, **validated_data)
        return mechanic
