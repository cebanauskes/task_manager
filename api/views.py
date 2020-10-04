from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from .filters import TaskFilter
from .models import Task
from .permissions import IsAuthor
from .serializers import TaskSerializer


class TaskViewSet(ModelViewSet):

    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated, IsAuthor)
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status', 'complete_date']
    filterset_class = TaskFilter

    def get_queryset(self):
        profile = self.request.user
        return Task.objects.filter(author=profile)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)