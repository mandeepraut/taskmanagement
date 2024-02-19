from django.contrib import admin
from .models import Task,Review

#Admin Username and password
# admin10 admin10

# Register your models here.
admin.site.register(Task)
admin.site.register(Review)