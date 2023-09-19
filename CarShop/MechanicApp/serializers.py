from rest_framework import serializers as mechanic_serializers
from Shared.models import Mechanic, User
from MachineParts.models import MachineParts

class MachinePartCreateSerializer(mechanic_serializers.ModelSerializer):

    class Meta:
        model = MachineParts
        fields = ['name', 'year', 'brand', 'price', 'tags', 'stock_capacity']#icon to be added same for mechanic


    def create(self, validated_data):
        owner_id = validated_data.pop('owner_id')
        owner_queryset = Mechanic.objects.filter(user_id=owner_id)
        if owner_queryset.count() == 0:
            return {'no': 'send'}
        owner = owner_queryset.first()
        machine_part = MachineParts.objects.create(owner=owner, **validated_data)
        return machine_part




