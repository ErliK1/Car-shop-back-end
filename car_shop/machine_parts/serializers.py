from rest_framework import serializers
from .models import MachinePart, Category


class MachinePartSerializerGeneral(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    owner = serializers.StringRelatedField()

    class Meta:
        model = MachinePart
        fields = ['id', 'name', 'serial_no', 'description', 'image', 'price', 'tags', 'material',
                  'brand', 'made_in', 'cateogry', 'owner']


class MachineCategories(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'image']


