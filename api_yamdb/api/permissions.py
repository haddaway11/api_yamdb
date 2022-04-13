from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    message = 'Изменение чужого контента запрещено!'

    def has_object_permission(self, request, view, obj):
<<<<<<< HEAD
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user


class IsAdminOrReadOnly(permissions.BasePermission):
    message = 'Действие доступно только администратору!'

    def has_permission(self, request, view):
        return (
            request.user in permissions.SAFE_METHODS
            or request.user.is_staff or request.user.role == 'admin'
        )
=======
        return (request.method in permissions.SAFE_METHODS
                or obj.author == request.user)


class IsModeratorOwnerAdminOrReadOnly(permissions.BasePermission):
   
    def has_object_permission(self, request, view, obj):
        return (request.method in permissions.SAFE_METHODS
                or obj.author == request.user
                or request.user.is_moderator
                or request.user.is_admin)


class IsAdminOrReadOnly(permissions.BasePermission):
   
    def has_object_permission(self, request, view, obj):
        return (request.method in permissions.SAFE_METHODS
                or request.user.is_admin)


class ReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS
>>>>>>> feauture/auth-users
