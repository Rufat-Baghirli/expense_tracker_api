from rest_framework import permissions

class IsOwner(permissions.BasePermission):
    """
    Custom permission to allow access only to objects that belong to the requesting user.
    """

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
