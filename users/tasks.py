import datetime
import os
import django
from celery import shared_task

from users.services import sending_notice

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from users.models import User


@shared_task
def notice_for_users():
    """
    Celery task to send notice emails to users who haven't visited the site for a long time.

    This task retrieves users who haven't logged in for more than 15 days and sends them a notice email.
    """
    time_for_notice = datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(days=15)
    user_for_notice = User.objects.filter(last_login__lt=time_for_notice, is_active=True)
    for user in user_for_notice:
        sending_notice(user.email, user.first_name)
