from rest_framework.permissions import BasePermission
from Shared.models import Mechanic
class MechanicPermission(BasePermission):

    def has_permission(self, request, view):
        if Mechanic.objects.filter(user=request.user).count() == 0:
            return False
        return True
