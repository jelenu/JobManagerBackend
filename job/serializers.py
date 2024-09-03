from rest_framework import serializers
from .models import Location, Worker, Tool, Job, ScheduledLocation

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = '__all__'

class ToolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tool
        fields = '__all__'

class JobSerializer(serializers.ModelSerializer):
    tools = ToolSerializer(many=True, read_only=True)

    class Meta:
        model = Job
        fields = '__all__'

class ScheduledLocationSerializer(serializers.ModelSerializer):
    location = LocationSerializer(read_only=True)
    jobs = JobSerializer(many=True, read_only=True)
    workers = WorkerSerializer(many=True, read_only=True)

    class Meta:
        model = ScheduledLocation
        fields = '__all__'
