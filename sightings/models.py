from django.db import models

class Squirrel(models.Model):
    latitude = models.CharField(max_length=100)
    longtitude = models.CharField(max_length=100)
    id = models.CharField(max_length=100,primary_key=True)
    date = models.DateField()
    shift = models.CharField(max_length=10)
    age = models.CharField(max_length=3)
    primary_fur_color = models.CharField(max_length=20)
    highlight_fur_color = models.CharField(max_length=20)
    location = models.CharField(max_length=30)
    running = models.BooleanField()
    chasing = models.BooleanField()
    climbing = models.BooleanField()
    eating = models.BooleanField()
    foraging = models.BooleanField()

    def __str__(self):
        return self.id
# Create your models here.
