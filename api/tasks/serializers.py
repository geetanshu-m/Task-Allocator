from rest_framework import serializers
from .models import (
    user,
    company,
    user_tasks
)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=user
        fields = "__all__"

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model=company
        fields = "__all__"

class TasksSerializer(serializers.ModelSerializer):
    class Meta:
        model=user_tasks
        fields = "__all__"