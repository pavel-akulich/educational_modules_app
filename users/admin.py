from django.contrib import admin

from users.models import User


@admin.register(User)
class UsersAdmin(admin.ModelAdmin):
    """
    Admin configuration for the User model.

    Attributes:
        list_display (tuple): Tuple containing the fields to be displayed in the admin list view.
    """

    list_display = ('pk', 'email', 'first_name', 'last_name', 'phone', 'country', 'avatar',)
