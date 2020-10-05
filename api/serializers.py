from django.utils import timezone
from rest_framework import serializers

from .models import Task, TaskHistory


class TaskSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    status = serializers.ChoiceField(choices=Task.STATUS_CHOICES, required=False)
    create_date = serializers.DateTimeField(required=False)

    def validate(self, data):

        if self.instance:
            if data['complete_date'] and data['complete_date'] < self.instance.create_date:
                raise serializers.ValidationError(
                    'Планируемая дата завершения раньше даты создания')
        else:
            if data['complete_date'] and data['complete_date'] < timezone.now():
                raise serializers.ValidationError(
                    'Планируемая дата завершения раньше текущей даты')
        
        return data

    class Meta:
        model = Task
        fields = (
            'id', 
            'title', 
            'description', 
            'author', 
            'create_date', 
            'status', 
            'complete_date',
        )


class TaskHistorySerializer(serializers.ModelSerializer):
    status = serializers.ChoiceField(choices=Task.STATUS_CHOICES, required=False)
    create_date = serializers.DateTimeField(required=False)
    
    class Meta:
        model = TaskHistory
        fields = (
            'id',
            'title',
            'description',
            'author',
            'create_date',
            'status',
            'complete_date',
            'edit_date',
        )