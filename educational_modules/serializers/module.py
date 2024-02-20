from rest_framework import serializers

from educational_modules.models import Module
from educational_modules.serializers.lesson import LessonSerializer


class ModuleSerializer(serializers.ModelSerializer):
    """
    Serializer for Module objects.

    Attributes:
        lessons_count (serializers.IntegerField): Field to represent the count of lessons in the module.
        lessons (LessonSerializer): Serializer for the lessons associated with the module.
        class Meta: Inner class containing metadata for the serializer.
    """

    lessons_count = serializers.IntegerField(source='lesson_set.all.count', required=False)
    lessons = LessonSerializer(source='lesson_set.all', many=True, required=False)

    class Meta:
        """
        Metadata for the ModuleSerializer.

        Attributes:
            model (Module): The model class associated with the serializer.
            fields (tuple): Tuple containing the fields to be serialized.
            read_only_fields (tuple): Tuple containing read-only fields.
        """
        model = Module
        fields = (
            'pk', 'title', 'description', 'preview', 'lessons_count', 'lessons', 'owner',)
        read_only_fields = ('owner',)
