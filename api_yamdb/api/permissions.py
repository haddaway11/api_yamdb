from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    message = 'Изменение чужого контента запрещено!'

    def has_object_permission(self, request, view, obj):
        return (request.method in permissions.SAFE_METHODS
                or obj.author == request.user)


class IsModerator(permissions.BasePermission):
   
    def has_object_permission(self, request, view, obj):
        return (request.method in permissions.SAFE_METHODS
                or request.user.is_moderator
                or request.user.is_admin
                or request.user.is_superuser)


class IsAdmin(permissions.BasePermission):
   
    def has_object_permission(self, request, view, obj):
        return (request.user.is_admin
                or request.user.is_superuser)


class ReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS
