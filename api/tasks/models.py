from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class company(models.Model):
    company_name = models.CharField(max_length=120)
    company_employees = models.ManyToManyField(User)
    class Meta:
        db_table = 'company'

class user_tasks(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task_title = models.CharField(max_length=120)
    task_detail = models.TextField()
    completed = models.BooleanField(default=False)
    createdAt = models.DateTimeField(default=timezone.now())