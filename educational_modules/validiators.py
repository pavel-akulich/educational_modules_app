from rest_framework import serializers

from educational_modules.models import Module


def validate_module_owner(value, user):
    """
    Validates if the user is the owner of the module.

    Args:
        value (Module): The module instance to be validated.
        user: The user instance to be checked against the module's owner.

    Returns:
        Module: The validated module instance.

    Raises:
        serializers.ValidationError: If the passed value is not a Module instance,
            or if the module does not have an owner attribute, or if the user is not the owner of the module.
    """

    if not isinstance(value, Module):
        raise serializers.ValidationError('The passed value is not a module.')

    if not hasattr(value, 'owner'):
        raise serializers.ValidationError('The module does not have an owner attribute.')

    if value.owner != user:
        raise serializers.ValidationError("You can't create lessons for other people's modules!")

    return value
