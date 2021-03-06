from django_filters import rest_framework as filters
from .models import Task


class TaskFilter(filters.FilterSet):
    date_from = filters.DateTimeFilter(field_name='complete_date', lookup_expr='gte')
    date_to = filters.DateTimeFilter(field_name='complete_date', lookup_expr='lte')

    class Meta:
        model = Task
        fields = ['status', 'date_from', 'date_to',]