from django.db import models
# from django.contrib.auth.models import User
from django.utils import timezone

'''
TODO

Extending the Django base user schema for the User table
'''
class user(models.Model):
    user_name = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    createdAt = models.DateTimeField(default=timezone.now)
    class Meta:
        db_table = 'user'
    
class company(models.Model):
    company_name = models.CharField(max_length=120, unique=True)
    company_employees = models.ManyToManyField(user)
    class Meta:
        db_table = 'company'

class user_tasks(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    task_title = models.CharField(max_length=120)
    task_detail = models.TextField()
    completed = models.BooleanField(default=False)
    createdAt = models.DateTimeField(default=timezone.now)