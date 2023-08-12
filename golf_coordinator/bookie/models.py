from django.db import models
from bookie import models
from golf_trip.models import *
from GolfRound.models import *
from django.utils import timezone



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
    ]

    bet_tee_time = models.ForeignKey(Trip_TeeTime, related_name='golfbet_tee_time', on_delete=models.PROTECT)
    submitter = models.ForeignKey(Trip_Golfer, related_name='submitter', on_delete=models.PROTECT)
    opponent = models.ForeignKey(Trip_Golfer, related_name='opponent', on_delete=models.PROTECT)
    units = models.DecimalField(max_digits=5, decimal_places=2)
    bet_closed = models.BooleanField(default=False)
    bet_winner = models.ForeignKey(Trip_Golfer, related_name='winner', blank=True, null=True,  on_delete=models.PROTECT)
    bet_timestamp = models.DateTimeField(auto_now_add=True)
    bet_type = models.CharField(choices=CHOICES, default='1', max_length=255)

    def get_bet_scores(self):

        scores = []

        # if self.bet_closed and len(scores) == 0:
        #     winning_score = self.bet_tee_time.net_rounds().fiter(tee_time__tee__course_name=self.opponent.tee_time.tee.course_name).filter(round_golfer=self.submitter.full_name()).values()[0]['net_score']

        if self.bet_closed:
            try:
                winning_score = Net_Round_Score.objects.all().filter(tee_time__tee__course__course_name=self.bet_tee_time.tee.course.course_name).filter(round_golfer=self.submitter.full_name()).values()[0]['net_score']
                losing_score = self.bet_tee_time.net_rounds().filter(round_golfer=self.opponent.full_name()).values()[0]['net_score']
                scores.append(winning_score)
                scores.append(losing_score)
            except IndexError:
                pass
        
        else:
            scores = [0,0]

        return scores
    

    def __str__(self):
        return "{}_{}_{}_{}".format(self.bet_tee_time.id, self.submitter, self.opponent, self.bet_type)
    


class TeamVsTeam(GolfBet):
    """Where someone can bet on which team wins in a particular round
    """
    tee_time = models.ForeignKey(Trip_TeeTime, related_name='TVT_submitter_tee_time', on_delete=models.PROTECT)
    submitter_selected_team = models.ForeignKey(Trip_Team, related_name='submitter_selected_team', on_delete=models.PROTECT)