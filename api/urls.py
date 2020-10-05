from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import TaskViewSet, TaskHistoryView

router = DefaultRouter()
router.register('tasks', TaskViewSet, basename='tasks')

urlpatterns = [
    path('', include(router.urls)),
    path('tasks/<int:task_id>/history/', TaskHistoryView.as_view(), name='history'),
]