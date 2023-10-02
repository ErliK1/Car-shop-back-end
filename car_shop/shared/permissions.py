from rest_framework.permissions import BasePermission
from .models import Mechanic

class MechanicPermission(BasePermission):

    def has_permission(self, request, view):
        if Mechanic.objects.filter(user=request.user).exists():
            return True
        return False

    def has_object_permission(self, request, view, obj):
        return obj.id == Mechanic.objects.get(user=request.user)


