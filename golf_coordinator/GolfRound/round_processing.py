from golf_trip.models import Trip_Team

def round_processing(round_formset_data, tee_data):
    '''
    This function is responsible for taking the data from the teetime, and the submitted round.
    It will calculate each players net and gross score.


    Once all of that information is gathered, it will be passed to determine_team_scores()
    '''

    # used for calculating course_handicap
    course_slope = tee_data.tee.slope
    course_rating = tee_data.tee.rating
    course_par = tee_data.tee.course_par

    team_data = Trip_Team.objects.all()

    teetime_score_data = []
    for players_round in round_formset_data:
        # grab golfer
        round_golfer = players_round.cleaned_data['round_golfer']

        # golfers assigned team
        golfer = tee_data.Players.all().filter(golfer__last_name=round_golfer)
        
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
         #before maniuplating the data, setting the raw_holes to the gross score.

        stroking_holes = []
        for idx, hole_hcp in enumerate(course_hole_hcp_index):
            # if a player is a 13, this will populate the stroking_holes list with the index of which holes those 13 are.
            if player_course_hcp >= hole_hcp:
                stroking_holes.append(idx)

       
        # adjust each raw score based on HCP and max ESG

        #empty lists to hold the gross and net scores
        gross_score = []
        net_score = []

        # had to use extend because if it was net_score=raw_score, anything that got updated for net_score would update raw. Extend lets you create a copy of a list 
        net_score.extend(raw_score)
        gross_score.extend(raw_score)


        # stroking_holes contains the index of which holes the player gets handicap assistance.
        for stroke in stroking_holes:

            # getting the players score on the hole he gets a stroke
            net_hole_score = net_score[stroke]

            # getting the par of that hole
            hole_par = course_hole_par[stroke]

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

                adjusted_hole_score = hole_par + 2 + strokes
                raw_score[stroke] = adjusted_hole_score
            else:
                adjusted_hole_score = net_hole_score - strokes
                raw_score[stroke] = adjusted_hole_score


        #calculating totals
        total_net_score = sum(raw_score)
        total_gross_score = sum(gross_score)

        # context data that gets passed to teetime_score_data for each golfer
        player_score_data = {'golfer': round_golfer, 'team': golfer_team, 'net_score': raw_score, 'gross_score': gross_score, 'total_net_score': total_net_score, 'total_gross_score': total_gross_score }

        teetime_score_data.append(player_score_data)

    return teetime_score_data


def course_handicap_calculation(index, course_slope, course_rating, course_par):
    '''
    Used the USGA Handicap formula: https://www.usga.org/content/usga/home-page/handicapping/roh/Content/rules/6%201%20Course%20Handicap%20Calculation.htm
    '''
    course_handicap = index * (course_slope/113) + (course_rating - course_par)
    return course_handicap



# This would work for 1v1 games as well. Doesn't support scrambles
def determine_2v2_team_scores(teetime_score_data, team_name_1, team_name_2, teetime_gametype):
    '''
    This function takes the processed round data, and will determine the scores

    this is accomplished by determining which players are on the same team

    the team score will get passed into teetime_team_scores to process the two golfer scores into 1 team score. This is done in teetime_team_scores.

    Once the team scores have been gathered, the gametype for the teetime will be evaluated. Depending on the gametype, the function to calucate the score will change

    '''
    ################taking the 4 golfers from the teetime data, and breaking them up into two teams#####################
    team_1 = []
    team_2 = []

    #it looks gross, but i'm using the index for the teetime_score_data so I could more easily compare values in the list 
    for golfer in range(len(teetime_score_data)):
        #['team'] is a queryset object, so the index has to be passed in to use the data
        # I want to look at not passing in the team_name as a variable to the function, but was a quicker solution for now
        if teetime_score_data[golfer]['team'][0].team == team_name_1:
            team_1.append(teetime_score_data[golfer])
        elif teetime_score_data[golfer]['team'][0].team == team_name_2:
            team_2.append(teetime_score_data[golfer])
        else: 
            raise Exception
    team_1_score = teetime_team_scores(team_1)
    team_2_score = teetime_team_scores(team_2)

    if teetime_gametype == '2v2 best ball':
        final_results = determine_bestball_win_stroke(team_1_score, team_2_score)
    elif teetime_gametype == '2v2 best ball - matchplay':
        final_results = determine_bestball_win_match(team_1_score, team_2_score)
    # print('team_1_score: {}'.format(team_1_score))
    # print('team_2_score: {}'.format(team_2_score))
    # print('final_results: {}'.format(final_results))
    return final_results


############once the player's teams are determined, the players' scores are looped through, to determine the "best ball" for each hole##############
def teetime_team_scores(team_list):
    '''
    the return value from determine_team_scores() is passed in for each team. Right now this only supports teams of 2.
    '''
    teammate_1 = team_list[0]
    teammate_2 = team_list[1]

    team_score = []

    #this for loop is comparing teammate_1's score to teammate_2. This is to figure out who had the best score for each hole
    for index in range(len(teammate_1['net_score'])):

        if teammate_1['net_score'][index] <= teammate_2['net_score'][index]:
            team_score.append(teammate_1['net_score'][index])
        else:
            team_score.append(teammate_2['net_score'][index])
    return team_score



############Using the data from bestball_team_score, the two team's bestball scores are compared and determined which team wins######################
def determine_bestball_win_stroke(team_1_score, team_2_score):
    '''
    This only focuses on 1 scoreline, and team_1 is set as the baseline. so if they are -12, that means team 1 lost by 12 strokes.
    '''
    team_1_bestball_stroke_score = []

    # this for loop looks at each hole's score for team 1 and compares it to score for team 2. Used indexes so it's easier to compare between the two teams 
    for index in range(len(team_1_score)):

        if team_1_score[index] <= team_2_score[index]:
            score_diff = team_2_score[index] - team_1_score[index]
            team_1_bestball_stroke_score.append(score_diff)
        else:
            score_diff = team_2_score[index] - team_1_score[index]
            team_1_bestball_stroke_score.append(score_diff)

    net_stroke_sum = sum(team_1_bestball_stroke_score)
    score_dict = {'team_1': team_1_bestball_stroke_score, 'net_score': net_stroke_sum}
    return score_dict


def determine_bestball_win_match(team_1_score, team_2_score):
    '''
    This only focuses on 1 scoreline, and team_1 is set as the baseline. so if they are -3, that means team 1 lost by 3 holes.
    '''
    team_1_bestball_match_score = []

    for index in range(len(team_1_score)):
        if team_1_score[index] < team_2_score[index]:
            score_diff = 1
            team_1_bestball_match_score.append(score_diff)
        elif team_1_score[index] == team_2_score[index]:
            score_diff = 0
        else:
            score_diff = -1
            team_1_bestball_match_score.append(score_diff)

    net_match_sum = sum(team_1_bestball_match_score)
    score_dict = {'team_1': team_1_bestball_match_score, 'net_score': net_match_sum}
    return score_dict










