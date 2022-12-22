from django.db import models

# Create your models here.

class ZaigoUsers(models.Model):
    name = models.CharField(max_length=20)
    dateofbirth = models.DateField()
    address = models.CharField(max_length=30)
    status = models.SmallIntegerField(default=1)