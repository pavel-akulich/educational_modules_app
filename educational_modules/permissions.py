from rest_framework.permissions import BasePermission


class IsModerator(BasePermission):
    """
    Permission class to check if the user is a moderator.

    Attributes:
        message (str): The error message to be displayed if the permission check fails.
    """
    message = 'You are not a moderator!'

    def has_permission(self, request, view):
        """
        Checks if the user is a moderator.

        Args:
            request: The request object.
            view: The view object.

        Returns:
            bool: True if the user is a moderator, False otherwise.
        """
        if request.user.groups.filter(name='moderator').exists():
            return True
        return False


class IsNotModerator(BasePermission):
    """
    Permission class to check if the user is not a moderator.

    Attributes:
        message (str): The error message to be displayed if the permission check fails.
    """
    message = 'Moderators cannot create lessons or modules!'

    def has_permission(self, request, view):
        """
        Checks if the user is not a moderator.

        Args:
            request: The request object.
            view: The view object.

        Returns:
            bool: True if the user is not a moderator, False otherwise.
        """
        if not request.user.groups.filter(name='moderator').exists():
            return True
        return False


class IsSuperUser(BasePermission):
    """
    Permission class to check if the user is a superuser.

    Attributes:
        message (str): The error message to be displayed if the permission check fails.
    """
    message = 'You are not a superuser!'

    def has_permission(self, request, view):
        """
        Checks if the user is a superuser.

        Args:
            request: The request object.
            view: The view object.

        Returns:
            bool: True if the user is a superuser, False otherwise.
        """
        if request.user.is_superuser:
            return True
        return False


class IsOwner(BasePermission):
    """
    Permission class to check if the user is the owner of an object.

    Attributes:
        message (str): The error message to be displayed if the permission check fails.
    """
    message = 'You are not the owner!'

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
        if request.user == obj.owner:
            return True
        return False
