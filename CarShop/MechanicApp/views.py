from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, CreateAPIView
from MachineParts.models import MachineParts
from .permissions import MechanicPermission
from .serializers import MachinePartCreateSerializer
# Create your views here.


class MachinePartCreateView(ListCreateAPIView):
    queryset = MachineParts.objects.all()
    serializer_class = MachinePartCreateSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            return [MechanicPermission(), ]
        return []

    def post(self, request, *args, **kwargs):
        serializer_instance: MachinePartCreateSerializer = self.get_serializer(data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.validated_data['owner_id'] = request.user.id
            data = serializer_instance.save()
            if isinstance(data, MachineParts):
                return Response(serializer_instance.validated_data, status=status.HTTP_201_CREATED)
            return Response({'message': 'ERROR'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer_instance.errors, status=status.HTTP_400_BAD_REQUEST)





