# Create your models here.
from django.db import models
from django.utils import timezone


class Todo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    dueDate_at = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.title