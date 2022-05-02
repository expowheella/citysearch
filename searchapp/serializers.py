
from .models import City
from rest_framework import serializers


class CitySerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=255)

    class Meta:
        # Each name is unique.
        model = City
        fields = ('name',)

    def create(self, validated_data):
        return City.objects.create(**validated_data)


