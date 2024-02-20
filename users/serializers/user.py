from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    """
Serializer for User objects.

Attributes:
    Meta class: Inner class containing metadata for the serializer.
"""
    password = serializers.CharField(write_only=True, required=False)

    def create(self, validated_data):
        """
        Create and return a new User instance with the validated data.

        Args:
            validated_data (dict): Dictionary containing the validated data.

        Returns:
            User: Newly created User instance.
        """
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        """
        Update and return an existing User instance with the validated data.

        Args:
            instance (User): Existing User instance to be updated.
            validated_data (dict): Dictionary containing the validated data.

        Returns:
            User: Updated User instance.
        """
        password = validated_data.pop('password', None)
        if password:
            instance.set_password(password)
        return super().update(instance, validated_data)

    class Meta:
        """
        Metadata for the UserSerializer.

        Attributes:
            model (User): The model class associated with the serializer.
            fields (tuple): Tuple containing the fields to be serialized.
        """
        model = User
        fields = ('pk', 'password', 'email', 'first_name', 'last_name', 'phone', 'country', 'avatar',)
