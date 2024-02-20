from django.contrib import admin

from educational_modules.models import Module, Lesson


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Module model.

    Attributes:
        list_display (tuple): Tuple containing the fields to be displayed in the admin list view.
    """
    list_display = ('pk', 'title', 'preview', 'description', 'owner',)


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Lesson model.

    Attributes:
        list_display (tuple): Tuple containing the fields to be displayed in the admin list view.
    """
    list_display = ('pk', 'title', 'description', 'preview', 'video_url', 'module', 'owner',)
