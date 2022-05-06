from django.db import models


class City(models.Model):
    name = models.CharField(max_length=10000, unique=True, primary_key=True, default=True)

    def __str__(self):
        return self.name
