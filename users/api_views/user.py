from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from educational_modules.permissions import IsSuperUser, IsModerator
from users.models import User
from users.permissions import IsOwner
from users.serializers.user import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing User objects.

    Attributes:
        serializer_class (UserSerializer): The serializer class for User objects.
        queryset (QuerySet): The queryset for User objects.
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_permissions(self):
        """
        Returns the list of permissions based on the action performed.

        Returns:
            list: List of permission classes.
        """
        if self.action == 'list':
            permission_classes = [IsSuperUser | IsModerator]
        elif self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsSuperUser | IsOwner]
        elif self.action == 'destroy':
            permission_classes = [IsSuperUser]
        elif self.action == 'retrieve':
            permission_classes = [IsSuperUser | IsOwner | IsModerator]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
