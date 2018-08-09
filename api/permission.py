from rest_framework.permissions import BasePermission

class IsTeacher(BasePermission):
    message = 'you shall not pass'

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff or obj.owner == request.user:
            return True
        return False