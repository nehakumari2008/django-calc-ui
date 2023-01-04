from django.db import models


# Create your models here.
from django.utils import timezone


class Operation(models.Model):
    first_number = models.IntegerField(default=0)
    second_number = models.IntegerField(default=0)
    operator = models.CharField(max_length=1)
    Result = models.IntegerField()
    Created_on = models.DateTimeField(default=timezone.now())
