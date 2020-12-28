from rest_framework.response import Response
from rest_framework import viewsets
from tasks.serializers import (
    UserSerializer,
    CompanySerializer,
    TasksSerializer
)
from tasks.models import (
    user,
    company,
    user_tasks
)

class UserView(viewsets.ModelViewSet):
    queryset = user.objects.all()
    serializer_class = UserSerializer

class CompanyView(viewsets.ModelViewSet):
    queryset = company.objects.all()
    serializer_class = CompanySerializer

class UserTaskView(viewsets.ModelViewSet):
    queryset = user_tasks.objects.all()
    serializer_class = TasksSerializer