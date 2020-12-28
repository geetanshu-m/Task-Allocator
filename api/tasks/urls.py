from django.urls import path
from tasks.viewsets.userViewset import (
    UserView,
    CompanyView,
    UserTaskView
)
from rest_framework import routers

router = routers.DefaultRouter()
router.register('user', UserView)
router.register('company', CompanyView)
router.register('task', UserTaskView)

urlpatterns = router.urls