from django.db import models


# Create your models here.
class Warehouse(models.Model):
    location_name = models.CharField(max_length=100)    # location_name VARCHAR(100)
    manager = models.CharField(max_length=100)


class Visitor(models.Model):
    visitor_name = models.CharField(max_length=150)
    time_of_visit = models.DateTimeField(auto_now=True)
    purchases = models.TextField()
