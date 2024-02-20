from rest_framework import generics
from rest_framework.filters import SearchFilter

from educational_modules.models import Module
from educational_modules.paginators import ModulePaginator
from educational_modules.permissions import IsOwner, IsModerator, IsNotModerator, IsSuperUser
from educational_modules.serializers.module import ModuleSerializer


class ModuleCreateAPIView(generics.CreateAPIView):
    """
    API view for creating a Module instance.

    Attributes:
        serializer_class (ModuleSerializer): The serializer class for Module objects.
        permission_classes (list): List of permission classes.
    """
    serializer_class = ModuleSerializer

    def perform_create(self, serializer):
        """
        Performs creation of a Module object.

        Args:
            serializer: The serializer instance.
        """
        serializer.save(owner=self.request.user)

    permission_classes = [IsNotModerator]


class ModuleListAPIView(generics.ListAPIView):
    """
    API view for listing Module instances.

    Attributes:
        serializer_class (ModuleSerializer): The serializer class for Module objects.
        queryset (QuerySet): The queryset for Module objects.
        pagination_class (ModulePaginator): The paginator class for Module objects.
        filter_backends (list): List of filter backends applied to the view.
        search_fields (list): List of fields that can be searched using search filter.
    """
    serializer_class = ModuleSerializer
    queryset = Module.objects.all()
    pagination_class = ModulePaginator
    filter_backends = [SearchFilter]
    search_fields = ['title', 'description']

    def get_queryset(self):
        """
        Returns the queryset based on the user's role.

        Returns:
            QuerySet: Filtered queryset.
        """
        if self.request.user.groups.filter(name='moderator').exists() or self.request.user.is_superuser:
            return Module.objects.all()
        return Module.objects.filter(owner=self.request.user)


class ModuleRetrieveAPIView(generics.RetrieveAPIView):
    """
    API view for retrieving a Module instance.

    Attributes:
        serializer_class (ModuleSerializer): The serializer class for Module objects.
        queryset (QuerySet): The queryset for Module objects.
        permission_classes (list): List of permission classes.
    """
    serializer_class = ModuleSerializer
    queryset = Module.objects.all()
    permission_classes = [IsOwner | IsModerator | IsSuperUser]


class ModuleUpdateAPIView(generics.UpdateAPIView):
    """
    API view for updating a Module instance.

    Attributes:
        serializer_class (ModuleSerializer): The serializer class for Module objects.
        queryset (QuerySet): The queryset for Module objects.
        permission_classes (list): List of permission classes.
    """
    serializer_class = ModuleSerializer
    queryset = Module.objects.all()
    permission_classes = [IsOwner | IsModerator | IsSuperUser]


class ModuleDestroyAPIView(generics.DestroyAPIView):
    """
    API view for destroying a Module instance.

    Attributes:
        queryset (QuerySet): The queryset for Module objects.
        permission_classes (list): List of permission classes.
    """
    queryset = Module.objects.all()
    permission_classes = [IsOwner | IsSuperUser]
