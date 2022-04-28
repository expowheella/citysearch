from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_headers
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import City
from .serializers import CitySerializer
from django.http import JsonResponse
from rest_framework import status, generics
from django.db import IntegrityError
from django.core.cache import cache
import json


class GetCity(APIView):


    def get(self, request):
        serializer = CitySerializer(data=request.data)
        serializer.is_valid()

        cities_id = request.data["city_id"]

        if cache.get(cities_id):
            city = cache.get(cities_id)
            print(f'GET from cache {city}')

            content = {
                "name": city,

            }
            return JsonResponse({"name": str(city),
                                 "city_id": cities_id}
                                ,safe=False)

            # return Response(json.loads('{city}'))


        else:

            try:


                city = City.objects.get(city_id=cities_id)
                print("PUT in cash")
                cache.set(
                    cities_id,
                    city
                    # request.data
                )
                print('GET from database')




            except City.DoesNotExist:
                return Response({'Not exist in db'})


        print('GET from database')
        return Response({'name': serializer.data})




    # def post(self, request, *args, **kwargs):
    #     city_id = kwargs["city_id"]
    #     serializer = CitySerializer(data=request.data)
    #
    #     try:
    #         if serializer.is_valid():
    #             serializer.save()
    #             print(serializer.data)
    #             # cache.set({'name'}, serializer.data, timeout=None)
    #             cache.set(key='city_id', serializer.data, timeout=None)
    #             print(f'выполнен POST-запрос {serializer.data}')
    #             return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     except IntegrityError:
    #         print(f'Не выполнен POST-запрос {request.data}')
    #         return Response({'name': serializer.data})
