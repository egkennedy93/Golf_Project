# from django.test import TestCase
import os
import django
import random


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'golf_coordinator.settings')
django.setup()

from golf_trip.models import Trip_TeeTime
from GolfRound.models import Round_Score, Net_Round_Score

def score_definer(hole_par, player_hcp):
    #data from https://golfingfocus.com/how-often-should-you-hit-your-golf-handicap-its-good-news/
    scoring_per_handicap = {'1_5': {'bird': 1.5/18, 'par': 9/18, 'bogey': 5.9/18, 'd_bogey': 1.3/18, 'alot': .3/18}, 
                    '6_10':{'bird': .9/18, 'par': 7/18, 'bogey': 7.3/18, 'd_bogey': 2.3/18, 'alot': .5/18},
                    '11_15': {'bird': .5/18, 'par': 5.1/18, 'bogey': 7.7/18, 'd_bogey': 3.5/18, 'alot': 1.1/18},
                    '16_20': {'bird': .3/18, 'par': 3.6/18, 'bogey': 7.3/18, 'd_bogey': 4.7/18, 'alot': 2.1/18},
                    '21_25': {'bird': .2/18, 'par': 2.5/18, 'bogey': 6.3/18, 'd_bogey': 5.5/18, 'alot': 3.4/18},}


    if player_hcp <= 5:
        score_percentage = scoring_per_handicap['1_5']
    elif player_hcp >= 5 and player_hcp <= 10:
        score_percentage = scoring_per_handicap['6_10']
    elif player_hcp >= 11 and player_hcp <= 15:
        score_percentage = scoring_per_handicap['11_15']
    elif player_hcp >= 16 and player_hcp <= 20:
        score_percentage = scoring_per_handicap['16_20']
    elif player_hcp >= 21 and player_hcp <= 25:
        score_percentage = scoring_per_handicap['21_25']

    if hole_par == 3:
        possible_scores = [1,2,3,4,5,6,7]
        randomList = random.choices(possible_scores, weights=(.00008, score_percentage['bird']*100, score_percentage['par']*100, score_percentage['bogey']*100, score_percentage['d_bogey']*100, score_percentage['alot']*100, .001))
    if hole_par == 4:
        possible_scores = [2,3,4,5,6,7,8]
        randomList = random.choices(possible_scores, weights=(.02, score_percentage['bird']*100, score_percentage['par']*100, score_percentage['bogey']*100, score_percentage['d_bogey']*100, score_percentage['alot']*100, .001))

    if hole_par == 5:
        possible_scores = [3,4,5,6,7,8,9]
        randomList = random.choices(possible_scores, weights=(.001, score_percentage['bird']*100, score_percentage['par']*100, score_percentage['bogey']*100, score_percentage['d_bogey']*100, score_percentage['alot']*100, .001))


    return randomList[0]


def test_get_tee_times():
    first_tee_time = Trip_TeeTime.objects.get(pk=1)
    # tee_time_players = first_tee_time.Players.all()

    tee_hole_par = [first_tee_time.tee.hole_1_par,
                    first_tee_time.tee.hole_2_par,
                    first_tee_time.tee.hole_3_par,
                    first_tee_time.tee.hole_4_par,
                    first_tee_time.tee.hole_5_par,
                    first_tee_time.tee.hole_6_par,
                    first_tee_time.tee.hole_7_par,
                    first_tee_time.tee.hole_8_par,
                    first_tee_time.tee.hole_9_par,
                    first_tee_time.tee.hole_10_par,
                    first_tee_time.tee.hole_11_par,
                    first_tee_time.tee.hole_12_par,
                    first_tee_time.tee.hole_13_par,
                    first_tee_time.tee.hole_14_par,
                    first_tee_time.tee.hole_15_par,
                    first_tee_time.tee.hole_16_par,
                    first_tee_time.tee.hole_17_par,
                    first_tee_time.tee.hole_18_par,]




    for player in first_tee_time.Players.all():
        player_round_score = Round_Score.objects.create(tee_time=first_tee_time, 
                                                        round_golfer=player.golfer.last_name,
                                                        golfer_index=player.hcp_index,
                                                        hole_1_score = score_definer(tee_hole_par[0], player.hcp_index),
                                                        hole_2_score = score_definer(tee_hole_par[1], player.hcp_index),
                                                        hole_3_score = score_definer(tee_hole_par[2], player.hcp_index),
                                                        hole_4_score = score_definer(tee_hole_par[3], player.hcp_index),
                                                        hole_5_score = score_definer(tee_hole_par[4], player.hcp_index),
                                                        hole_6_score = score_definer(tee_hole_par[5], player.hcp_index),
                                                        hole_7_score = score_definer(tee_hole_par[6], player.hcp_index),
                                                        hole_8_score = score_definer(tee_hole_par[7], player.hcp_index),
                                                        hole_9_score = score_definer(tee_hole_par[8], player.hcp_index),
                                                        hole_10_score = score_definer(tee_hole_par[9], player.hcp_index),
                                                        hole_11_score = score_definer(tee_hole_par[10], player.hcp_index),
                                                        hole_12_score = score_definer(tee_hole_par[11], player.hcp_index),
                                                        hole_13_score = score_definer(tee_hole_par[12], player.hcp_index),
                                                        hole_14_score = score_definer(tee_hole_par[13], player.hcp_index),
                                                        hole_15_score = score_definer(tee_hole_par[14], player.hcp_index),
                                                        hole_16_score = score_definer(tee_hole_par[15], player.hcp_index),
                                                        hole_17_score = score_definer(tee_hole_par[16], player.hcp_index),
                                                        hole_18_score = score_definer(tee_hole_par[17], player.hcp_index),
                                                        total_score = 250,
                                                        net_score = 180,
                                                        )
        
        player_round_score = Net_Round_Score.objects.create(tee_time=first_tee_time, 
                                                        round_golfer=player.golfer.last_name,
                                                        hole_1_score = score_definer(tee_hole_par[0], player.hcp_index),
                                                        hole_2_score = score_definer(tee_hole_par[1], player.hcp_index),
                                                        hole_3_score = score_definer(tee_hole_par[2], player.hcp_index),
                                                        hole_4_score = score_definer(tee_hole_par[3], player.hcp_index),
                                                        hole_5_score = score_definer(tee_hole_par[4], player.hcp_index),
                                                        hole_6_score = score_definer(tee_hole_par[5], player.hcp_index),
                                                        hole_7_score = score_definer(tee_hole_par[6], player.hcp_index),
                                                        hole_8_score = score_definer(tee_hole_par[7], player.hcp_index),
                                                        hole_9_score = score_definer(tee_hole_par[8], player.hcp_index),
                                                        hole_10_score = score_definer(tee_hole_par[9], player.hcp_index),
                                                        hole_11_score = score_definer(tee_hole_par[10], player.hcp_index),
                                                        hole_12_score = score_definer(tee_hole_par[11], player.hcp_index),
                                                        hole_13_score = score_definer(tee_hole_par[12], player.hcp_index),
                                                        hole_14_score = score_definer(tee_hole_par[13], player.hcp_index),
                                                        hole_15_score = score_definer(tee_hole_par[14], player.hcp_index),
                                                        hole_16_score = score_definer(tee_hole_par[15], player.hcp_index),
                                                        hole_17_score = score_definer(tee_hole_par[16], player.hcp_index),
                                                        hole_18_score = score_definer(tee_hole_par[17], player.hcp_index),
                                                        total_score = 250,
                                                        net_score = 180,
                                                        )


if __name__ == '__main__':
    print('here')
    test_get_tee_times()
        
