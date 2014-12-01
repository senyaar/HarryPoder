from rest_framework import serializers
from .models import Kitty, Shelter, GENDER_CHOICES, BREED_CHOICES, STATUS_CHOICES

class ShelterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shelter
        fields = ('name',)

class KittySerializer(serializers.ModelSerializer):
    location = ShelterSerializer(source='location')

    class Meta:
        model = Kitty
        photo = serializers.Field('photo.url')
        fields = ('name', 'gender', 'age', 'breed', 'weight', 'about', 'photo', 'location', )