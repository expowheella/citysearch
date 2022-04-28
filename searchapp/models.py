from django.db import models


class City(models.Model):
    # exist = models.BooleanField(default=True)
    name = models.CharField(max_length=255, unique=True)
    city_id = models.IntegerField(primary_key=True, default=True)

    def __str__(self):
        return self.name
