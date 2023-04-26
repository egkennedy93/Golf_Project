from django.db import models
from bookie import models
from golf_trip.models import * 



# Model that extends the contrib.auth package to support golfer specific attributes.
# after developing more, it made more sense to have handicaps associated with the trip, and not the user model. Might have a overall 
# handicap at a later date 

# four bet types:
# --yourself vs someone
# -- you and someone else are betting on the outcome of a 1v1
# --betting on which team wins in your teetime
# -- you and someone else are betting on the outcome of a teetime

class GolfBet(models.Model):
    """Basic class for a GolfBet. This is intended to be inherited and never directly used

    """
    CHOICES = [
        ('1', 'Bet against Player'),
        ('2', 'Bet against Team'),
    ]

    bet_tee_time = models.ForeignKey(Trip_TeeTime, related_name='golfbet_tee_time', on_delete=models.PROTECT)
    submitter = models.ForeignKey(Trip_Golfer, related_name='submitter', on_delete=models.PROTECT)
    opponent = models.ForeignKey(Trip_Golfer, related_name='opponent', on_delete=models.PROTECT)
    units = models.DecimalField(max_digits=5, decimal_places=2)
    bet_closed = models.BooleanField(default=False)
    bet_winner = models.ForeignKey(Trip_Golfer, related_name='winner', blank=True, null=True,  on_delete=models.PROTECT)
    bet_timestamp = models.DateTimeField(auto_now_add=True)
    bet_type = models.CharField(choices=CHOICES, default='1', max_length=255)
    


class TeamVsTeam(GolfBet):
    """Where someone can bet on which team wins in a particular round
    """
    tee_time = models.ForeignKey(Trip_TeeTime, related_name='TVT_submitter_tee_time', on_delete=models.PROTECT)
    submitter_selected_team = models.ForeignKey(Trip_Team, related_name='submitter_selected_team', on_delete=models.PROTECT)