from django.db import models

class Location(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Worker(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Tool(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Job(models.Model):
    name = models.CharField(max_length=255)
    tools = models.ManyToManyField(Tool, blank=True) 

    def __str__(self):
        return self.name    


class ScheduledLocation(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    date = models.DateField()
    jobs = models.ManyToManyField(Job)
    workers = models.ManyToManyField(Worker)

    def __str__(self):
        return f'{self.location.name} on {self.date}'
