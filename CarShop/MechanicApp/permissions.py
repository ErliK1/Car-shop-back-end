from rest_framework.permissions import BasePermission
from Shared.models import Mechanic
class MechanicPermission(BasePermission):

    def has_permission(self, request, view):
        if Mechanic.objects.filter(user_id=request.user.id).count() == 0:
            return False
        return True
