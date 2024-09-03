from rest_framework import viewsets
from .models import Location, Worker, Tool, Job, ScheduledLocation
from .serializers import LocationSerializer, WorkerSerializer, ToolSerializer, JobSerializer, ScheduledLocationSerializer

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class WorkerViewSet(viewsets.ModelViewSet):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer

class ToolViewSet(viewsets.ModelViewSet):
    queryset = Tool.objects.all()
    serializer_class = ToolSerializer

class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

class ScheduledLocationViewSet(viewsets.ModelViewSet):
    queryset = ScheduledLocation.objects.all()
    serializer_class = ScheduledLocationSerializer
