from django.conf import settings
from django.core.mail import send_mail


def sending_notice(email, username):
    """
    Sends a notice email to remind the user to visit the site.

    Args:
        email (str): The email address of the recipient.
        username (str): The username of the recipient.
    """
    send_mail(
        subject='Educational Modules',
        message=f"{username}, You haven't visited our site for a long time to learn something new, come back! ",
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email]
    )
