from django.db import models


class Types(models.Model):
    type = models.CharField(max_length=100)

    def __str__(self):
        return self.type
