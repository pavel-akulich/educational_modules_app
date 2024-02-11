from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated

from educational_modules.models import Lesson
from educational_modules.paginators import LessonPaginator
from educational_modules.permissions import IsNotModerator, IsOwner, IsSuperUser, IsModerator
from educational_modules.serializers.lesson import LessonSerializer


class LessonViewSet(viewsets.ModelViewSet):
    """
    A view set for handling CRUD operations on Lesson objects.

    Attributes:
        serializer_class (LessonSerializer): The serializer class for Lesson objects.
        queryset (QuerySet): The queryset for Lesson objects.
        pagination_class (LessonPaginator): The paginator class for Lesson objects.
        filter_backends (list): List of filter backends applied to the view.
        search_fields (list): List of fields that can be searched using search filter.
    """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    pagination_class = LessonPaginator
    filter_backends = [SearchFilter]
    search_fields = ['title', 'description', 'content']

    def get_permissions(self):
        """
        Returns the list of permissions based on the action performed.

        Returns:
            list: List of permission classes.
        """
        if self.action == 'create':
            permission_classes = [IsNotModerator]
        elif self.action == 'retrieve':
            permission_classes = [IsOwner | IsModerator | IsSuperUser]
        elif self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsOwner | IsModerator | IsSuperUser]
        elif self.action == 'destroy':
            permission_classes = [IsOwner | IsSuperUser]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        """
        Returns the queryset based on the user's role.

        Returns:
            QuerySet: Filtered queryset.
        """
        if self.request.user.groups.filter(name='moderator').exists() or self.request.user.is_superuser:
            return Lesson.objects.all()
        return Lesson.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        """
        Performs creation of a Lesson object.

        Args:
            serializer: The serializer instance.
        """
        serializer.save(owner=self.request.user)
