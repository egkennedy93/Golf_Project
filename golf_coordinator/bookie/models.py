from django.db import models
from bookie import models
from golf_trip.models import * 



# Model that extends the contrib.auth package to support golfer specific attributes.
# after developing more, it made more sense to have handicaps associated with the trip, and not the user model. Might have a overall 
# handicap at a later date 

class GolfBet(models.Model):
    
    submitter = models.ForeignKey(Trip_Golfer, on_delete=models.PROTECT)
    units = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    
    
class PlayerVsPlayer(GolfBet):
    submitter_tee_time = models.ForeignKey(Trip_TeeTime, related_name='submitter_tee_time', on_delete=models.PROTECT)
    opponent_tee_time = models.ForeignKey(Trip_TeeTime, related_name='opponent_tee_time', on_delete=models.PROTECT)
    opponent_bet = models.ForeignKey(Trip_Golfer, on_delete=models.PROTECT)


class TeamVsTeam(GolfBet):
    submitter_tee_time = models.ForeignKey(Trip_TeeTime, related_name='submitter_tee_time', on_delete=models.PROTECT)
    opponent_tee_time = models.ForeignKey(Trip_TeeTime, related_name='opponent_tee_time', on_delete=models.PROTECT)
    bet_initiator_team = models.ForeignKey(Trip_Team, related_name='initiator_team', on_delete=models.PROTECT)
    bet_opponent_team = models.ForeignKey(Trip_Team, related_name='opponet_team', on_delete=models.PROTECT)