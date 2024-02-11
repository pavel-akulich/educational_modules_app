from rest_framework import serializers

from educational_modules.models import Lesson
from educational_modules.validiators import validate_module_owner


class LessonSerializer(serializers.ModelSerializer):
    """
    Serializer for Lesson objects.

    Attributes:
        class Meta: Inner class containing metadata for the serializer.
    """

    class Meta:
        """
        Metadata for the LessonSerializer.

        Attributes:
            model (Lesson): The model class associated with the serializer.
            fields (tuple): Tuple containing the fields to be serialized.
        """
        model = Lesson
        fields = ('pk', 'title', 'description', 'preview', 'video_url', 'content', 'module', 'owner',)

    def validate_module(self, module_value):
        """
        Validates the module ownership.

        Args:
            module_value: The value of the module field.

        Returns:
            Module: The validated module instance.

        Raises:
            serializers.ValidationError: If the user is not the owner of the module.
        """
        user = self.context['request'].user
        return validate_module_owner(module_value, user)
