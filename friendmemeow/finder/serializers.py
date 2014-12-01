from rest_framework import serializers
from .models import Kitty, Shelter, GENDER_CHOICES, BREED_CHOICES, STATUS_CHOICES

class KittySerializer(serializers.ModelSerializer):
    pk = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, max_length=20)
    location = serializers.CharField(required=True)
    gender = serializers.ChoiceField(choices=GENDER_CHOICES, default='M')
    age = serializers.IntegerField(default=1)
    breed = serializers.ChoiceField(choices=BREED_CHOICES, default='Un')
    weight = serializers.IntegerField(default=5)
    about = serializers.CharField(style={'type': 'textarea'})
    photo = serializers.ImageField(null=True)
    posted_date = serializers.DateTimeField(default=timezone.now)
    status = serializers.ChoiceField(choices=STATUS_CHOICES, default='Need')

    def create(self, validated_attrs):
        return Kitty.objects.create(**validated_attrs)

    def update(self, instance, validated_attrs):
        instance.name = validated_attrs.get('name', instance.name)
        instance.location = validated_attrs.get('location', instance.location)
        instance.gender = validated_attrs.get('gender', instance.gender)
        instance.age = validated_attrs.get('age', instance.age)
        instance.breed = validated_attrs.get('breed', instance.breed)
        instance.weight = validated_attrs.get('weight', instance.weight)
        instance.about = validated_attrs.get('about', instance.about)
        instance.photo = validated_attrs.get('photo', instance.photo)
        instance.posted_date = validated_attrs.get('posted_date', instance.posted_date)
        instance.status = validated_attrs.get('status', instance.status)
        instance.save()
        return instance