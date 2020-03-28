from django.conf import settings
from django.db import models
from django.utils import timezone


class Customer(models.Model):
    employee = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=20)
    mobile = models.CharField(max_length=15)
    
        
    created_date = models.DateTimeField(default=timezone.now)
    join_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name
        
        
        
class Generator(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    capacitie = models.IntegerField(blank=True, null=True)
    working = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
        
        
        
class SubLine(models.Model):
    Generator = models.ForeignKey(Generator, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    capacitie = models.IntegerField(blank=True, null=True)
    working = models.BooleanField(default=True)
    
    
    def __str__(self):
        return self.name
        
        
        
        
        
        
        