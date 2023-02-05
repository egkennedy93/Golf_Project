from django.contrib import admin
from GolfRound.models import Round_Score, Net_Round_Score
from golf_trip.models import Trip_TeeTime, Trip_Golfer

# Register your models here.


@admin.register(Round_Score, Net_Round_Score)
class GolfRoundAdmin(admin.ModelAdmin):
    pass