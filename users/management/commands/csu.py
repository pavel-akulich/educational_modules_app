from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    """
    Management command to create a superuser.

    This command creates a superuser with the provided email, first name, last name, and password.
    """
    def handle(self, *args, **options):
        """
        Handle method for executing the command.

        Args:
            *args: Additional arguments.
            **options: Additional keyword arguments.
        """
        user = User.objects.create(
            email='enter_your_email',
            first_name='enter_your_first_name',
            last_name='enter_your_last_name',
            is_staff=True,
            is_superuser=True
        )

        user.set_password('enter_your_password')
        user.save()
