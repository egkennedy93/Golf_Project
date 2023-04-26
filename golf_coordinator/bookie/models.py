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
    
    submitter = models.ForeignKey(Trip_Golfer, related_name='submitter', on_delete=models.PROTECT)
    opponent = models.ForeignKey(Trip_Golfer, related_name='opponent', on_delete=models.PROTECT)
    units = models.DecimalField(max_digits=5, decimal_places=2)
    bet_closed = models.BooleanField(default=False)
    bet_winner = models.ForeignKey(Trip_Golfer, related_name='winner', blank=True, null=True, default="N/A",  on_delete=models.PROTECT)
    test = models.CharField(max_length=500, default="test")
    
class TeeTimeBet(GolfBet):
    bet_tee_time = models.ForeignKey(Trip_TeeTime, related_name='bet_tee_time', on_delete=models.PROTECT)

    
class PlayerVsPlayer(GolfBet):
    """Handles a bet between two people directly. THey can be in the same or different teetimes. 
    """
    submitter_tee_time = models.ForeignKey(Trip_TeeTime, related_name='PVP_submitter_tee_time', on_delete=models.PROTECT)
    opponent_tee_time = models.ForeignKey(Trip_TeeTime, related_name='opponent_tee_time', on_delete=models.PROTECT)
    


class ThirdPartyPlayerVsPlayer(GolfBet):
    """This is similar to PlayerVsPlayer except its two people betting on the outcome of a round they aren't playing in.
    """
    player_1 = models.ForeignKey(Trip_Golfer, related_name='player_1', on_delete=models.PROTECT)
    player_2 = models.ForeignKey(Trip_Golfer, related_name='player_2', on_delete=models.PROTECT)
    submitter_tee_time = models.ForeignKey(Trip_TeeTime, related_name='player_1_tee_time', on_delete=models.PROTECT)
    opponent_tee_time = models.ForeignKey(Trip_TeeTime, related_name='player_2_tee_time', on_delete=models.PROTECT)



class TeamVsTeam(GolfBet):
    """Where someone can bet on which team wins in a particular round
    """
    tee_time = models.ForeignKey(Trip_TeeTime, related_name='TVT_submitter_tee_time', on_delete=models.PROTECT)
    submitter_selected_team = models.ForeignKey(Trip_Team, related_name='submitter_selected_team', on_delete=models.PROTECT)