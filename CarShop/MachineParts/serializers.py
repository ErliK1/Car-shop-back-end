from rest_framework import serializers
from .models import MachineParts


class MachinePartsSerializer(serializers.ModelSerializer):

    class Meta:
        model = MachineParts
        fields = '__all__'
