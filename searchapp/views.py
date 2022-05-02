from rest_framework.views import APIView
from rest_framework.response import Response

from searchapp.serializers import CitySerializer
from .models import City
from django.http import JsonResponse
from django.core.cache import cache
from django.db import IntegrityError

class GetCity(APIView):
    def get(self, request):

        city_name = request.data["name"]
        print(city_name)

        if cache.get(city_name):
            city = cache.get(city_name)
            print(f'GET from cache {city}')
            return JsonResponse({"name": str(city)}, safe=False)

        else:

            try:
                city = City.objects.get(name=city_name)
                print("PUT in cash")
                cache.set(city_name, city_name)
                print('GET from database')

            except City.DoesNotExist:
                serializer = CitySerializer(data=request.data)
                try:
                    if serializer.is_valid():
                        serializer.save()
                        print(f"{city_name} is added in the db")
                        return Response({'New city is added into the database'})
                except IntegrityError:
                    print(f'POST-request is failed {request.data}')
                    return Response({'no such city'})

        print('GET from database')
        return JsonResponse({"name": str(city)}, safe=False)



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
