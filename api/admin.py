from django.contrib import admin

from .models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'description',
        'author', 'status', 
        'create_date', 'complete_date',)


admin.site.register(Task, TaskAdmin)