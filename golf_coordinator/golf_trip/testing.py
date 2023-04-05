# from django.test import TestCase
import os
import django
import random


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'golf_coordinator.settings')
django.setup()

from golf_trip.models import Trip_TeeTime
from GolfRound.models import Round_Score, Net_Round_Score
from GolfRound import round_processing

first_tee_time = Trip_TeeTime.objects.get(pk=1)

# function that defines what score a player will shoot based on their handicap

def score_definer(hole_par, player_hcp):
    '''
    hole_par:int => defines what par the hole is.
    player_hcp:int => defines what the players handicap is

    using these two variables, the percentage odds of getting a certain score can be determined
    '''
    #data from https://mygolfspy.com/labs/study-overall-golfer-performance-by-handicap/
    scoring_per_handicap = {'1_5': {'bird': 1.5/18, 'par': 9/18, 'bogey': 5.9/18, 'd_bogey': 1.3/18, 'alot': .3/18}, 
                    '6_10':{'bird': .9/18, 'par': 7/18, 'bogey': 7.3/18, 'd_bogey': 2.3/18, 'alot': .5/18},
                    '11_15': {'bird': .5/18, 'par': 5.1/18, 'bogey': 7.7/18, 'd_bogey': 3.5/18, 'alot': 1.1/18},
                    '16_20': {'bird': .3/18, 'par': 3.6/18, 'bogey': 7.3/18, 'd_bogey': 4.7/18, 'alot': 2.1/18},
                    '21_25': {'bird': .2/18, 'par': 2.5/18, 'bogey': 6.3/18, 'd_bogey': 5.5/18, 'alot': 3.4/18},}

    # based on handicap scoring_percentage variable gets associated with the aligned handicap dictionary
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

    # for everything in these if blocks, +4 is the highest a score can go 
    if hole_par == 3:
        possible_scores = [1,2,3,4,5,6,7]
        randomList = random.choices(possible_scores, weights=(.00008, 
                                                              score_percentage['bird']*100, 
                                                              score_percentage['par']*100, 
                                                              score_percentage['bogey']*100, 
                                                              score_percentage['d_bogey']*100, 
                                                              score_percentage['alot']*100, .001))
    if hole_par == 4:
        possible_scores = [2,3,4,5,6,7,8]
        randomList = random.choices(possible_scores, weights=(.02, 
                                                              score_percentage['bird']*100, 
                                                              score_percentage['par']*100, 
                                                              score_percentage['bogey']*100, 
                                                              score_percentage['d_bogey']*100, 
                                                              score_percentage['alot']*100, .001))

    if hole_par == 5:
        possible_scores = [3,4,5,6,7,8,9]
        randomList = random.choices(possible_scores, weights=(.001, 
                                                              score_percentage['bird']*100, 
                                                              score_percentage['par']*100, 
                                                              score_percentage['bogey']*100, 
                                                              score_percentage['d_bogey']*100, 
                                                              score_percentage['alot']*100, .001))

    # returns the int value of the weighted value
    return randomList[0]


def calculate_net_score(player_course_hcp, player_score):

    course_hole_hcp_index = [first_tee_time.tee.hole_1_index,
                    first_tee_time.tee.hole_2_index,
                    first_tee_time.tee.hole_3_index,
                    first_tee_time.tee.hole_4_index,
                    first_tee_time.tee.hole_5_index,
                    first_tee_time.tee.hole_6_index,
                    first_tee_time.tee.hole_7_index,
                    first_tee_time.tee.hole_8_index,
                    first_tee_time.tee.hole_9_index,
                    first_tee_time.tee.hole_10_index,
                    first_tee_time.tee.hole_11_index,
                    first_tee_time.tee.hole_12_index,
                    first_tee_time.tee.hole_13_index,
                    first_tee_time.tee.hole_14_index,
                    first_tee_time.tee.hole_15_index,
                    first_tee_time.tee.hole_16_index,
                    first_tee_time.tee.hole_17_index,
                    first_tee_time.tee.hole_18_index,]
    
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
        
    stroking_holes = []
    for idx, hole_hcp in enumerate(course_hole_hcp_index):
        # if a player is a 13, this will populate the stroking_holes list with the index of which holes those 13 are.
        if player_course_hcp >= hole_hcp:
            stroking_holes.append(idx)

    #empty lists to hold the gross and net scores
    gross_score = player_score
    net_score = []

    # had to use extend because if it was net_score=raw_score, anything that got updated for net_score would update raw. Extend lets you create a copy of a list 
    net_score.extend(player_score)
    
    


    # stroking_holes contains the index of which holes the player gets handicap assistance.
    for stroke in stroking_holes:

        # getting the players score on the hole he gets a stroke
        net_hole_score = net_score[stroke]

        # getting the par of that hole
        hole_par = tee_hole_par[stroke]

        # getting the index difficulty of the hole
        hole_index = course_hole_hcp_index[stroke]

        # this logic is for handling if someone is aboe a 18 handicap
        # example if the player is a 20, then 20-18 = 2. If the hole is the 1 or 2 handicap hole, the player gets two strokes  
        if player_course_hcp - 18 >= hole_index:
            strokes = 2
        
        # player gets a normal stroke of 1 
        else:
            strokes = 1

        # this is handling net double bogey. If there score is over the holes net double bogey, it gets set to net double bogey
        if net_hole_score > hole_par + 2 + strokes:

            adjusted_hole_score = hole_par + 2
            net_score[stroke] = adjusted_hole_score
        else:
            adjusted_hole_score = net_hole_score - strokes
            net_score[stroke] = adjusted_hole_score

    #calculating totals
    total_net_score = sum(net_score)

    return net_score


# This is the function that actually creates the tee times and uses the function called above
def test_get_tee_times():
    # will update this to hopefully do all tee times, not just 1 
    

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
        #course handicap
        CHCP = round_processing.course_handicap_calculation(player.hcp_index, first_tee_time.tee.slope, first_tee_time.tee.rating, first_tee_time.tee.course_par)
        scores = []
        for i in range(18):
            scores.append(score_definer(tee_hole_par[i], CHCP))

        

        Round_Score.objects.create(tee_time=first_tee_time, 
                                    round_golfer=player.golfer.last_name,
                                    golfer_index=CHCP,
                                    hole_1_score = score_definer(tee_hole_par[0], CHCP),
                                    hole_2_score = score_definer(tee_hole_par[1], CHCP),
                                    hole_3_score = score_definer(tee_hole_par[2], CHCP),
                                    hole_4_score = score_definer(tee_hole_par[3], CHCP),
                                    hole_5_score = score_definer(tee_hole_par[4], CHCP),
                                    hole_6_score = score_definer(tee_hole_par[5], CHCP),
                                    hole_7_score = score_definer(tee_hole_par[6], CHCP),
                                    hole_8_score = score_definer(tee_hole_par[7], CHCP),
                                    hole_9_score = score_definer(tee_hole_par[8], CHCP),
                                    hole_10_score = score_definer(tee_hole_par[9], CHCP),
                                    hole_11_score = score_definer(tee_hole_par[10], CHCP),
                                    hole_12_score = score_definer(tee_hole_par[11], CHCP),
                                    hole_13_score = score_definer(tee_hole_par[12], CHCP),
                                    hole_14_score = score_definer(tee_hole_par[13], CHCP),
                                    hole_15_score = score_definer(tee_hole_par[14], CHCP),
                                    hole_16_score = score_definer(tee_hole_par[15], CHCP),
                                    hole_17_score = score_definer(tee_hole_par[16], CHCP),
                                    hole_18_score = score_definer(tee_hole_par[17], CHCP),
                                    total_score = sum(scores),
                                    net_score = sum(calculate_net_score(CHCP, scores)),
                                    )
        
        Net_Round_Score.objects.create(tee_time=first_tee_time, 
                                        round_golfer=player.golfer.last_name,
                                        hole_1_score = score_definer(tee_hole_par[0], CHCP),
                                        hole_2_score = score_definer(tee_hole_par[1], CHCP),
                                        hole_3_score = score_definer(tee_hole_par[2], CHCP),
                                        hole_4_score = score_definer(tee_hole_par[3], CHCP),
                                        hole_5_score = score_definer(tee_hole_par[4], CHCP),
                                        hole_6_score = score_definer(tee_hole_par[5], CHCP),
                                        hole_7_score = score_definer(tee_hole_par[6], CHCP),
                                        hole_8_score = score_definer(tee_hole_par[7], CHCP),
                                        hole_9_score = score_definer(tee_hole_par[8], CHCP),
                                        hole_10_score = score_definer(tee_hole_par[9], CHCP),
                                        hole_11_score = score_definer(tee_hole_par[10], CHCP),
                                        hole_12_score = score_definer(tee_hole_par[11], CHCP),
                                        hole_13_score = score_definer(tee_hole_par[12], CHCP),
                                        hole_14_score = score_definer(tee_hole_par[13], CHCP),
                                        hole_15_score = score_definer(tee_hole_par[14], CHCP),
                                        hole_16_score = score_definer(tee_hole_par[15], CHCP),
                                        hole_17_score = score_definer(tee_hole_par[16], CHCP),
                                        hole_18_score = score_definer(tee_hole_par[17], CHCP),
                                        total_score = sum(scores),
                                        net_score = sum(calculate_net_score(CHCP, scores))
                                        )
        



if __name__ == '__main__':
    test_get_tee_times()
        
