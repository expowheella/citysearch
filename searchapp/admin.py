from django.contrib import admin
from .models import City

# register application -> to access through admin panel
admin.site.register(City)
