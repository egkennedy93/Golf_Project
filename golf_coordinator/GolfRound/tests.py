from django.test import TestCase
from golf_trip.models import Trip_Team
# Create your tests here.

team_data = Trip_Team.objects.all()

def course_handicap_calculation(index, course_slope, course_rating, course_par):
    course_handicap = index * (course_slope/113) + (course_rating - course_par)
    return course_handicap



# grab course hcp index
golfer_index = 0

course_hole_hcp_index = [15, 17, 7, 13, 3, 9, 1, 5, 11, 2, 12, 10, 8, 14, 18, 4, 16, 6]
course_hole_par = [5, 3, 5, 4, 5, 3, 4, 4, 3, 4, 5, 4, 3, 4, 5, 4, 3, 4]
raw_score = [5, 3, 5, 4, 5, 3, 4, 4, 3, 4, 5, 4, 3, 4, 5, 4, 3, 4]
print(' raw score: {}'.format(raw_score))


# determine players course handicap

# this should end up being 13
player_course_hcp = round(course_handicap_calculation(golfer_index, 140, 72.7, 72))
print('course hcp: {}' .format(player_course_hcp))





  # get which holes the player gets strokes
stroking_holes = []
for idx, hole_hcp in enumerate(course_hole_hcp_index):
    if player_course_hcp >= hole_hcp:
        stroking_holes.append(idx)
print('stroking holes:{}'.format(stroking_holes))


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

