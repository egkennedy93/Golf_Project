from django.contrib import admin
from golf_trip.models import Golf_Trip, Trip_Course, Trip_Team, Trip_Golfer, Trip_Event, Trip_TeeTime, Trip_TeamMember
import re
from django.shortcuts import get_object_or_404
# Register your models here.

admin.site.register(Golf_Trip)
admin.site.register(Trip_Course)
admin.site.register(Trip_Team)
admin.site.register(Trip_Event)
admin.site.register(Trip_TeamMember)

@admin.register(Trip_Golfer)
class Trip_GolferAdmin(admin.ModelAdmin):
    list_display = ('trip', 'golfer', 'hcp_index', 'score')
    list_filter = ('trip', 'golfer', 'hcp_index',)


@admin.register(Trip_TeeTime)
class Trip_TeeTimeAdmin(admin.ModelAdmin):
    list_filter = ('trip',)
    def formfield_for_manytomany(self, db_field, request, **kwargs):
        filtered_trip_pk = request.GET.get('_changelist_filters', '')
        trip_pk_rex = re.search(r"\d", filtered_trip_pk)
        trip_pk = int(trip_pk_rex.group())

        if db_field.name == "Players":
            kwargs["queryset"] = Trip_Golfer.objects.filter(trip=trip_pk)
        
        
        return super().formfield_for_manytomany(db_field, request, **kwargs)
         
