from abc import ABC

from rest_framework.renderers import JSONRenderer
from rest_framework.validators import UniqueTogetherValidator

from .models import City
from rest_framework import serializers


class CitySerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=255)

    class Meta:
        # Each name is unique.
        model = City
        fields = ('name', 'city_id')


        # validators = [
        #     UniqueTogetherValidator(
        #         queryset=City.objects.all(),
        #         fields=['__all__']
        #     )
        # ]

    def create(self, validated_data):
        return City.objects.create(**validated_data)


