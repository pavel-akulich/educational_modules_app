from django.conf import settings
from django.db import models

from users.models import NULLABLE


class Module(models.Model):
    """
    A class representing educational module.

    Attributes:
        title (CharField): The name of the module.
        description (TextField): Description of the module.
        preview (ImageField): Path to the preview image of the module.
        owner (User): The owner of the module.
    """
    title = models.CharField(max_length=150, verbose_name='module name')
    description = models.TextField(verbose_name='description of the module')
    preview = models.ImageField(upload_to='module_previews/', verbose_name='preview of module', **NULLABLE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, verbose_name='owner of the module',
                              **NULLABLE)

    def __str__(self):
        """
        Returns a string representation of the module.

        Returns:
            str: The title of the module.
        """
        return f'{self.title} {self.owner}'

    class Meta:
        verbose_name = 'module'
        verbose_name_plural = 'modules'


class Lesson(models.Model):
    """
    A class representing a lesson in a system of educational modules.

    Attributes:
        title (CharField): The name of the lesson.
        description (TextField): Description of the lesson.
        preview (ImageField): Field for storing the preview image of the lesson.
        video_url (URLField): The URL link to the video associated with the lesson.
        content (TextField): Content of the lesson.
        module (Module): The module to which the lesson belongs.
        owner (User): The owner of the lesson.
    """
    title = models.CharField(max_length=150, verbose_name='lesson name')
    description = models.TextField(verbose_name='description of the lesson')
    preview = models.ImageField(upload_to='lesson_previews/', verbose_name='preview of lesson', **NULLABLE)
    video_url = models.URLField(verbose_name='link to video', **NULLABLE)
    content = models.TextField(verbose_name='content of the lesson')

    module = models.ForeignKey(Module, on_delete=models.CASCADE, **NULLABLE, verbose_name='module')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, verbose_name='owner of the lesson',
                              **NULLABLE)

    def __str__(self):
        """
        Returns a string representation of the lesson.

        Returns:
            str: The title of the lesson.
        """
        return f'{self.title}'

    class Meta:
        verbose_name = 'lesson'
        verbose_name_plural = 'lessons'
