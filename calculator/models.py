from django.db import models

# Create your models here.
class Operation(models.Model):
    First_number = models.IntegerField()
    Second_number = models.IntegerField()
    operator = models.CharField(max_length = 1)
    Result = models.IntegerField()
    Created_on = models.DateField()