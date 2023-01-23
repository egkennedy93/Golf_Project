
def round_processing(round_formset_data, tee_data):

    course_slope = tee_data.tee.slope
    course_rating = tee_data.tee.rating
    course_par = tee_data.tee.course_par


    for players_round in round_formset_data:

        round_golfer = players_round.cleaned_data['round_golfer']
        golfer_index = players_round.cleaned_data['golfer_index']
        course_hcp = round(course_handicap_calculation(golfer_index, course_slope, course_rating, course_par))


        hole_1_score = players_round.cleaned_data['hole_1_score']
        hole_2_score = players_round.cleaned_data['hole_2_score']
        hole_3_score = players_round.cleaned_data['hole_3_score']
        hole_4_score = players_round.cleaned_data['hole_4_score']
        hole_5_score = players_round.cleaned_data['hole_5_score']
        hole_6_score = players_round.cleaned_data['hole_6_score']
        hole_7_score = players_round.cleaned_data['hole_7_score']
        hole_8_score = players_round.cleaned_data['hole_8_score']
        hole_9_score = players_round.cleaned_data['hole_9_score']
        hole_10_score = players_round.cleaned_data['hole_10_score']
        hole_11_score = players_round.cleaned_data['hole_11_score']
        hole_12_score = players_round.cleaned_data['hole_12_score']
        hole_13_score = players_round.cleaned_data['hole_13_score']
        hole_14_score = players_round.cleaned_data['hole_14_score']
        hole_15_score = players_round.cleaned_data['hole_15_score']
        hole_16_score = players_round.cleaned_data['hole_16_score']
        hole_17_score = players_round.cleaned_data['hole_17_score']
        hole_18_score = players_round.cleaned_data['hole_18_score']
        total_score = players_round.cleaned_data['total_score']
        net_score = players_round.cleaned_data['net_score']

      


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