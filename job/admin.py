from django.contrib import admin
from .models import Location, Worker, Tool, Job, ScheduledLocation

class JobInline(admin.TabularInline):
    model = Job
    extra = 1

class WorkerInline(admin.TabularInline):
    model = Worker
    extra = 1

class ScheduledLocationAdmin(admin.ModelAdmin):
    list_display = ('location', 'date')
    list_filter = ('date',)
    search_fields = ('location__name',)
    filter_horizontal = ('jobs', 'workers')

class JobAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    filter_horizontal = ('tools',)

class LocationAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class WorkerAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class ToolAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

admin.site.register(Location, LocationAdmin)
admin.site.register(Worker, WorkerAdmin)
admin.site.register(Tool, ToolAdmin)
admin.site.register(Job, JobAdmin)
admin.site.register(ScheduledLocation, ScheduledLocationAdmin)
