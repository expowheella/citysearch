from django.core.cache import cache
from django.core.cache.backends.locmem import LocMemCache
from django.forms import model_to_dict
from rest_framework import generics, status
from django.shortcuts import render
from rest_framework.renderers import JSONRenderer
import io
from rest_framework.parsers import JSONParser
from rest_framework.validators import UniqueTogetherValidator

import cities.settings as settings
from .models import City
from .serializers import CitySerializer
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.decorators import api_view
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_headers

from django.views.decorators.cache import cache_page
from django.core.cache.backends.base import DEFAULT_TIMEOUT

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)



# class CityAPIView(generics.ListAPIView):
#     queryset = City.objects.all()
#     serializer_class = CitySerializer


class CityAPIView(APIView):

    def get(self, request):# request содержит все параметры входящего get запроса
        val = request.data['name']
        if val in cache:
            return {'cache', cache.get('cities')}

        # check if city is in database and return True if it is there
        # elif City.objects.all().filter(name=request.data['name']).values().exists():
        # #     print('elif')
        #      return Response({'result': 'if True'})
        # return False if the city is new here, and add the new city in the database
        else:
            serializer = CitySerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()  # вызывыет метод CitySerializer.create()

            cache.set('name', serializer.save())

            # return Response({'cities': serializer.data})  # результат метода CitySerializer.create()
            return Response({'result': False})



    def post(self, request):  # request содержит все параметры входящего post запроса
        serializer = CitySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save() # вызывыет метод CitySerializer.create()


        return Response({'cities': serializer.data}) # результат метода CitySerializer.create()
#
#     if User.objects.filter(email=cleaned_info['username']).exists():
#     # at least one object satisfying query exists
#     else:
# # no object satisfying query exists

# @api_view(['GET'])
# def view_cached_cities(request):
#     if 'name' in cache:
#         # get results from cache
#         products = cache.get('name')
#         return Response(products, status=status.HTTP_201_CREATED)