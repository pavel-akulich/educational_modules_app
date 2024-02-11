from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """
    Permission class to check if the user is the owner of an object.

    Attributes:
        message (str): The error message to be displayed if the permission check fails.
    """
    message = 'You are not the owner of this profile!'

    def has_object_permission(self, request, view, obj):
        """
        Checks if the user is the owner of the object.

        Args:
            request: The request object.
            view: The view object.
            obj: The object being accessed.

        Returns:
            bool: True if the user is the owner, False otherwise.
        """
        if request.user == obj:
            return True
        return False
