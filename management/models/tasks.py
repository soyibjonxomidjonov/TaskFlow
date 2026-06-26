from django.db import models
from .employes import Employee

TASK_STATUS_CHOICES = [
    ('created', 'Created'),
    ('in_progress', 'In progress'),
    ('done', 'Done'),
]

class Task(models.Model):

    task_title = models.CharField(max_length=250, blank=False, null=False)
    task_description = models.TextField()

    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=50, choices=TASK_STATUS_CHOICES, default='created')

    due_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.task_title

    class Meta:
        ordering = ['-created_at']
