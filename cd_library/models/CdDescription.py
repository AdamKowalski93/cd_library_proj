from django.db import models
from .MusicTypes import Types


class CD(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    artist = models.CharField(max_length=40)
    date = models.DateField()
    type = models.ManyToManyField(Types)
