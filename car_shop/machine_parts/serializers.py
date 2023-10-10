from rest_framework import serializers
from .models import MachinePart, Category


class MachinePartCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MachinePart
        fields = ['id', 'name', 'serial_no', 'description', 'image', 'price', 'tags', 'material',
                  'brand', 'made_in', 'category']


class MachinePartSerializerGeneral(MachinePartCreateSerializer):
    category = serializers.StringRelatedField()
    owner = serializers.StringRelatedField()

    class Meta(MachinePartCreateSerializer.Meta):
        model = MachinePart
        fields = MachinePartCreateSerializer.Meta.fields + ['owner']


class MachineCategories(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'image']
