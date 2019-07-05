from django.db import models
from django.utils import timezone

# Create your models here.
class Todo(models.Model):
    
    PENDING = 0
    COMPLETED = 1
    STATUS_CHOICES = [
        (PENDING, 'pending'),
        (COMPLETED, 'completed'),
    ]
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    status = models.PositiveIntegerField(choices=STATUS_CHOICES, default=PENDING)
    creation_date = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    
    def __str__(self):
        return self.title