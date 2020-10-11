from django.db import models

class Squirrel(models.Model):
    id = models.CharField(
            max_length=100,
            help_text=('ID of squirrel'),
            primary_key=True
    )

    latitude = models.CharField(
            max_length=100,
            help_text=('Latitude'),
    )

    longtitude = models.CharField(
            max_length=100,
            help_text=('Longtitude'),
    )
    
    def __str__(self):
        return self.id
# Create your models here.
