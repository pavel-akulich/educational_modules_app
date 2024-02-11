from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    """
Serializer for User objects.

Attributes:
    Meta class: Inner class containing metadata for the serializer.
"""

    class Meta:
        """
        Metadata for the UserSerializer.

        Attributes:
            model (User): The model class associated with the serializer.
            fields (tuple): Tuple containing the fields to be serialized.
        """
        model = User
        fields = ('pk', 'email', 'first_name', 'last_name', 'phone', 'country', 'avatar',)
