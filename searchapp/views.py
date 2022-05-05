from rest_framework.views import APIView
from rest_framework.response import Response

from searchapp.serializers import CitySerializer
from .models import City
from django.http import JsonResponse
from django.core.cache import cache
from django.db import IntegrityError


class GetCity(APIView):
    def get(self, request):

        city_name = request.data["name"].title()
        # print(city_name)

        # looking for in cache
        if cache.get(city_name):
            city = cache.get(city_name)
            print(f'GET from cache {city}')
            # return JsonResponse({"name": str(city)}, safe=False)
            # ACCORDING TO THE TASK --> return True if the city exists
            return Response({True})
        else:
            # lookong for in db
            try:
                # if city exists in the db
                city = City.objects.get(name=city_name)
                print(f'GET from database & PUT in cache {city_name}')
                # and add it into cache
                cache.set(city_name, city_name)
                # return JsonResponse({"name": str(city)}, safe=False)
                # ACCORDING TO THE TASK --> return True if the city exists
                return Response({True})

            except City.DoesNotExist:
                # if city does not exist, add it in the db
                try:
                    serializer = CitySerializer(data=request.data)
                    if serializer.is_valid():
                        serializer.save()
                        print(f"ADD {city_name} in the db & cache")
                        # and add it into cache
                        cache.set(city_name, city_name)
                        # return Response({'New city is added into the database'})
                        # ACCORDING TO THE TASK --> return False if the city doesn't exist
                        return Response({False})

                except IntegrityError:
                    print(f'POST-request is failed {request.data}')
                    return Response({'no such city'})