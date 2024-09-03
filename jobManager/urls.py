from django.urls import path, include
from rest_framework.routers import DefaultRouter
from job.views import LocationViewSet, WorkerViewSet, ToolViewSet, JobViewSet, ScheduledLocationViewSet

router = DefaultRouter()
router.register(r'locations', LocationViewSet)
router.register(r'workers', WorkerViewSet)
router.register(r'tools', ToolViewSet)
router.register(r'jobs', JobViewSet)
router.register(r'scheduled_locations', ScheduledLocationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
