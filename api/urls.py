from django.urls import path, include

from rest_framework.routers import DefaultRouter
from tasks.views import TaskAPIView
from slots.views import SlotAPIView

router = DefaultRouter()
router.register('tasks', TaskAPIView, basename='task')
router.register('slots', SlotAPIView, basename='slot')

urlpatterns = router.urls
 