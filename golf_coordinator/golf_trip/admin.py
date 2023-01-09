from django.contrib import admin
from golf_trip.models import Golf_Trip, Trip_Course, Trip_Team, Trip_Golfer, Trip_Event
# Register your models here.

admin.site.register(Golf_Trip)
admin.site.register(Trip_Course)
admin.site.register(Trip_Team)
admin.site.register(Trip_Golfer)
admin.site.register(Trip_Event)

