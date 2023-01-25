from golf_trip.models import Trip_Team

def round_processing(round_formset_data, tee_data, teetime_data):


    course_slope = tee_data.tee.slope
    course_rating = tee_data.tee.rating
    course_par = tee_data.tee.course_par

    team_data = Trip_Team.objects.all()
    tee_time_golfers = tee_data.Players.all()


    for players_round in round_formset_data:
        player_score_data = {'golfer': round_golfer, 'team': golfer_team, 'score': final_score}
        # teams - red: Jason&Brett  blue: Everett&Michael

        # grab golfer
        round_golfer = players_round.cleaned_data['round_golfer']

        # golfers assigned team
        golfer = teetime_data.Players.all().filter(golfer__last_name=round_golfer)
        
        golfer_team=team_data.filter(members__pk=golfer[0].pk)

        # grab course hcp index
        golfer_index = players_round.cleaned_data['golfer_index']

        # determine players course handicap
        player_course_hcp = round(course_handicap_calculation(golfer_index, course_slope, course_rating, course_par))

        # get hcp index for each hole on the course
        course_hole_hcp_index = []
        course_hole_hcp_index.append(tee_data.tee.hole_1_index)
        course_hole_hcp_index.append(tee_data.tee.hole_2_index)
        course_hole_hcp_index.append(tee_data.tee.hole_3_index)
        course_hole_hcp_index.append(tee_data.tee.hole_4_index)
        course_hole_hcp_index.append(tee_data.tee.hole_5_index)
        course_hole_hcp_index.append(tee_data.tee.hole_6_index)
        course_hole_hcp_index.append(tee_data.tee.hole_7_index)
        course_hole_hcp_index.append(tee_data.tee.hole_8_index)
        course_hole_hcp_index.append(tee_data.tee.hole_9_index)
        course_hole_hcp_index.append(tee_data.tee.hole_10_index)
        course_hole_hcp_index.append(tee_data.tee.hole_11_index)
        course_hole_hcp_index.append(tee_data.tee.hole_12_index)
        course_hole_hcp_index.append(tee_data.tee.hole_13_index)
        course_hole_hcp_index.append(tee_data.tee.hole_14_index)
        course_hole_hcp_index.append(tee_data.tee.hole_15_index)
        course_hole_hcp_index.append(tee_data.tee.hole_16_index)
        course_hole_hcp_index.append(tee_data.tee.hole_17_index)
        course_hole_hcp_index.append(tee_data.tee.hole_18_index)
        
        # get players raw score per hole
        raw_score = []
        raw_score.append(players_round.cleaned_data['hole_1_score'])
        raw_score.append(players_round.cleaned_data['hole_2_score'])
        raw_score.append(players_round.cleaned_data['hole_3_score'])
        raw_score.append(players_round.cleaned_data['hole_4_score'])
        raw_score.append(players_round.cleaned_data['hole_5_score'])
        raw_score.append(players_round.cleaned_data['hole_6_score'])
        raw_score.append(players_round.cleaned_data['hole_7_score'])
        raw_score.append(players_round.cleaned_data['hole_8_score'])
        raw_score.append(players_round.cleaned_data['hole_9_score'])
        raw_score.append( players_round.cleaned_data['hole_10_score'])
        raw_score.append( players_round.cleaned_data['hole_11_score'])
        raw_score.append( players_round.cleaned_data['hole_12_score'])
        raw_score.append( players_round.cleaned_data['hole_13_score'])
        raw_score.append( players_round.cleaned_data['hole_14_score'])
        raw_score.append( players_round.cleaned_data['hole_15_score'])
        raw_score.append( players_round.cleaned_data['hole_16_score'])
        raw_score.append( players_round.cleaned_data['hole_17_score'])
        raw_score.append( players_round.cleaned_data['hole_18_score'])


        # grab the course hole par to handle ESG

        course_hole_par = []
        course_hole_par.append(tee_data.tee.hole_1_par)
        course_hole_par.append(tee_data.tee.hole_2_par)
        course_hole_par.append(tee_data.tee.hole_3_par)
        course_hole_par.append(tee_data.tee.hole_4_par)
        course_hole_par.append(tee_data.tee.hole_5_par)
        course_hole_par.append(tee_data.tee.hole_6_par)
        course_hole_par.append(tee_data.tee.hole_7_par)
        course_hole_par.append(tee_data.tee.hole_8_par)
        course_hole_par.append(tee_data.tee.hole_9_par)
        course_hole_par.append(tee_data.tee.hole_10_par)
        course_hole_par.append(tee_data.tee.hole_11_par)
        course_hole_par.append(tee_data.tee.hole_12_par)
        course_hole_par.append(tee_data.tee.hole_13_par)
        course_hole_par.append(tee_data.tee.hole_14_par)
        course_hole_par.append(tee_data.tee.hole_15_par)
        course_hole_par.append(tee_data.tee.hole_16_par)
        course_hole_par.append(tee_data.tee.hole_17_par)
        course_hole_par.append(tee_data.tee.hole_18_par)


        # get which holes the player gets strokes
        stroking_holes = []
        for idx, hole_hcp in enumerate(course_hole_hcp_index):
            if player_course_hcp >= hole_hcp:
                stroking_holes.append(idx)


        # adjust each raw score based on HCP and max ESG
        for stroke in stroking_holes:
            raw_hole_score = raw_score[stroke]
            hole_par = course_hole_par[stroke]
            hole_index = course_hole_hcp_index[stroke]

            if player_course_hcp - 18 >= hole_index:
                strokes = 2
            
            else:
                strokes = 1

            if raw_hole_score > hole_par + 2 + strokes:

                adjusted_hole_score = hole_par + 2 + strokes
                raw_score[stroke] = adjusted_hole_score
            else:
                adjusted_hole_score = raw_hole_score - strokes
                raw_score[stroke] = adjusted_hole_score

        final_score = raw_score



        # grab gametype

        # pass score data into gametype function

        ## first gametype to develope: 2v2 best ball 


def course_handicap_calculation(index, course_slope, course_rating, course_par):
    course_handicap = index * (course_slope/113) + (course_rating - course_par)
    return course_handicap



    

#     course_index_list.append(tee_data.tee.hole_1_index)
#     course_index_list.append(tee_data.tee.hole_2_index)
#     course_index_list.append(tee_data.tee.hole_3_index)
#     course_index_list.append(tee_data.tee.hole_4_index)
#     course_index_list.append(tee_data.tee.hole_5_index)
#     course_index_list.append(tee_data.tee.hole_6_index)
#     course_index_list.append(tee_data.tee.hole_7_index)
#     course_index_list.append(tee_data.tee.hole_8_index)
#     course_index_list.append(tee_data.tee.hole_9_index)
#     course_index_list.append(tee_data.tee.hole_10_index)
#     course_index_list.append(tee_data.tee.hole_11_index)
#     course_index_list.append(tee_data.tee.hole_12_index)
#     course_index_list.append(tee_data.tee.hole_13_index)
#     course_index_list.append(tee_data.tee.hole_14_index)
#     course_index_list.append(tee_data.tee.hole_15_index)
#     course_index_list.append(tee_data.tee.hole_16_index)
#     course_index_list.append(tee_data.tee.hole_17_index)
#     course_index_list.append(tee_data.tee.hole_18_index)

