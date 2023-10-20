from copy import deepcopy

from rest_framework import serializers
from .models import MachinePart, Category


class MachinePartCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MachinePart
        fields = ['id', 'name', 'serial_no', 'description', 'image', 'price', 'tags', 'material',
                  'brand', 'made_in', 'category']

    def update(self, instance: MachinePart, validated_data):
        category_data = validated_data.pop('category')
        instance.category.name = category_data.get('name', instance.category.name)
        instance.category.description = category_data.get('description', instance.category.description)
        instance.category.image = category_data.get('image', instance.category.image)
        instance.category.save()
        instance.name = validated_data.get('name', instance.name)
        instance.serial_no = validated_data.get('serial_no', instance.serial_no)
        instance.description = validated_data.get('description', instance.description)
        instance.image = validated_data.get('image', instance.image)
        instance.price = validated_data.get('price', instance.price)
        instance.tags = validated_data.get('tags', instance.tags)
        instance.material = validated_data.get('material', instance.material)
        instance.brand = validated_data.get('brand', instance.brand)
        instance.made_in = validated_data.get('made_in', instance.made_in)
        instance.save()
        return instance





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



