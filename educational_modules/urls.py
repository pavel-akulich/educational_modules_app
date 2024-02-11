from django.urls import path
from rest_framework.routers import DefaultRouter

from educational_modules.api_views.lesson import LessonViewSet
from educational_modules.api_views.module import ModuleCreateAPIView, ModuleListAPIView, ModuleRetrieveAPIView, \
    ModuleUpdateAPIView, ModuleDestroyAPIView
from educational_modules.apps import EducationalModulesConfig

app_name = EducationalModulesConfig.name

router = DefaultRouter()
router.register(r'lessons', LessonViewSet, basename='lessons')

urlpatterns = [
                  path('module/create/', ModuleCreateAPIView.as_view(), name='module-create'),
                  path('module/list/', ModuleListAPIView.as_view(), name='module-list'),
                  path('module/detail/<int:pk>/', ModuleRetrieveAPIView.as_view(), name='module-detail'),
                  path('module/update/<int:pk>/', ModuleUpdateAPIView.as_view(), name='module-update'),
                  path('module/delete/<int:pk>/', ModuleDestroyAPIView.as_view(), name='module-delete'),
              ] + router.urls
