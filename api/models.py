from django.db import models
from model_utils import Choices

from users.models import User


class Task(models.Model):
    STATUS_CHOICES = Choices(
        'new', 
        'planned',
        'performing', 
        'completed')
    # [
    #     ('NEW', 'Новая'),
    #     ('PLANNED', 'Запланированная'),
    #     ('IN PROGRESS', 'В работе'),
    #     ('COMPLETED', 'Завершенная'),
    # ]
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=5000)
    create_date = models.DateTimeField(
        'Дата создания', auto_now_add=True)
    status = models.TextField(
        choices=STATUS_CHOICES, default=STATUS_CHOICES.new)
    complete_date = models.DateTimeField(
        'Планируемая дата завершения', blank=True, null=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='tasks')


