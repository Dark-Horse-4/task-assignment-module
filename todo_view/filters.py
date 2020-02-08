import django_filters
from .models import Task


class AssigneeFilter(django_filters.FilterSet):
    
    class Meta:
        model = Task
        fields = ('assignee',)