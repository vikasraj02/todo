from django.db import models

# Create your models here.
class Task(models.Model):
    task = models.CharField(max_length=255)
    is_complete = models.BooleanField(default=False)
    completed_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.task
