from django.db import models

from users.models import User


class BaseTask(models.Model):

    STATUS_CHOICES = [
        ('NEW', 'Новая'),
        ('PLANNED', 'Запланированная'),
        ('IN_PROGRESS', 'В работе'),
        ('COMPLETED', 'Завершенная'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField(max_length=5000)
    create_date = models.DateTimeField(
        'Дата создания', auto_now_add=True)
    status = models.TextField(
        choices=STATUS_CHOICES, default='NEW')
    complete_date = models.DateTimeField(
        'Планируемая дата завершения', blank=True, null=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE)

    class Meta:
        abstract = True

    
class TaskHistory(BaseTask):
     
    edit_date = models.DateTimeField(
        'Дата изменения', auto_now_add=True)
    task = models.ForeignKey(
        'Task', on_delete=models.CASCADE, related_name='changes')


    class Meta:
        ordering = ('-create_date',)


class Task(BaseTask):

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        TaskHistory.objects.create(
            title=self.title, description=self.description,
            create_date=self.create_date, status=self.status,
            complete_date=self.complete_date, author=self.author,
            task=self)

    class Meta:
        ordering = ('-create_date',)