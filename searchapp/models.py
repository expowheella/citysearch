from django.db import models


class City(models.Model):
    # exist = models.BooleanField(default=True)
    name = models.CharField(max_length=255, unique=True, primary_key=True, default='City Name')

    def __str__(self):
        return self.name
