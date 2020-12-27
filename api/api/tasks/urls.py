from .views import (
    hello_world
)
from django.urls import path

urlpatterns = [
    path('hello', hello_world)
]