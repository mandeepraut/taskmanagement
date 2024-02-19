from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta

class Task(models.Model):
    STATUS_CHOICES = [
        ('open', 'Open'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]

    title = models.CharField(max_length=100,null=True)
    description = models.CharField(max_length=100,null=True) 

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='open')
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    # Provide a default value for the deadline field, for example, a month from today
    deadline = models.DateField(default=datetime.now() + timedelta(days=30))

    created_at = models.DateTimeField(auto_now_add=True, blank=False, )

    updated_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.title


    

    


