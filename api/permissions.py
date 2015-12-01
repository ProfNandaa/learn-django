from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    '''
    Custom permissions to only allow owners of an object to edit it.
    '''

    def has_object_permission(self, request, view, obj):
        # Read permission are allowed to any request
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the question
        return obj.owner == request.user