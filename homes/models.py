from django.db import models

# Create your models here.
class House(models.Model):
    address = models.CharField(max_length=300)
    house_name = models.CharField(max_length=100)
    door_code = models.CharField(max_length=50)
    gate_code = models.CharField(max_length=50)
    community_pool = models.CharField(max_length=50)
    fitness_center = models.CharField(max_length=50, blank=True, null=True)
    wifi_network = models.CharField(max_length=100, blank=True, null=True)
    wifi_password = models.CharField(max_length=100, blank=True, null=True)
    who_cares = models.CharField(max_length=50)
    observations = models.TextField(blank=True, null=True)
    
