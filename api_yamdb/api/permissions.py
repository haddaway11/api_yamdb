from rest_framework import permissions


class AuthorModerAdmOrRead(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method not in permissions.SAFE_METHODS:
            return request.user.is_authenticated
        return True

    def has_object_permission(self, request, view, obj):

        return (
            request.method in permissions.SAFE_METHODS or (
                obj.author == request.user) or (
                    request.user.role in ('moderator', 'admin')
            )
        )

        # return (
        #     (
        #         obj.author == request.user or (
        #             request.user.role in ('moderator', 'admin')
        #         )
        #     ) or request.method in permissions.SAFE_METHODS
        # )
