from django.contrib import admin
from django.urls import path
from django.views.decorators.cache import cache_page
from searchapp.views import GetCity

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', GetCity.as_view()),
]


