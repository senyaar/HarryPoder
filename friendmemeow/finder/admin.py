from django.contrib import admin

# from .models import Kitty, Shelter
from finder.models import Kitty, Shelter

admin.site.register(Kitty)
admin.site.register(Shelter)
