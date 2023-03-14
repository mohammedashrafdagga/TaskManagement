from rest_framework.permissions import BasePermission
from .utils import get_user_token


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        user = get_user_token(request)
        return obj.leader == user
