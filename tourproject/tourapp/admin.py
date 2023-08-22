from django.contrib import admin
from.models import travel
from .models import world
from.models import place
from.models import person


# Register your models here.
admin.site.register(place)
admin.site.register(world)
admin.site.register(travel)
admin.site.register(person)
