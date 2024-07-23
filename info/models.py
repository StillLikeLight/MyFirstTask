from django.db import models


class Info(models.Model):
    phone_number = models.CharField(max_length=11)
    address = models.CharField(max_length=11)
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    sOrb = models.CharField(max_length=6)
    file_license = models.FileField()

