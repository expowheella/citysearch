from django.contrib import admin
from django.urls import path

from searchapp.views import CityAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/citylist/', CityAPIView.as_view()),
    # path('api/v1/citylist/', view_cached_cities)# связь url-адреса с API-view
]
