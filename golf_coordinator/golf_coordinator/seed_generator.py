import os 
import django
import random
from Courses.models import Golf_Course


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'golf_coordinator.settings')
django.setup()


courses = ['Premier', 'Signature', 'Masterpiece', 'Tradition', 'Threetops', 'Himalayas']

premier_par_holes = [4,5,4,3,4,5,4,3,4,4,3,5,4,4,4,5,3,4]
premier_index_holes = [5,11,1,13,17,15,3,7,9,8,16,10,4,2,18,12,14,6]
premier_course_par = 72
premier_data = {'black': {'hole_yardage': [431,517,421,162,313,499,373,183,406,407,195,485,396,451,362,546,214,471], 'slope':139, 'rating': 73.3, 'yardage':6832}}

def add_course(course_choice):
    c = Golf_Course.objects.get_or_create(course_name=course_choice)[0]
    c.save()
    return c

premier = add_course(courses[0])

def add_tee(course_pk):
    for key in premier_data: 
        print(key)   
        # course_name = key
        # tee_name=premier_data
        # course_par = premier_course_par 
        # slope = premier_data[key][slope]
        # rating = premier_data[key]
        # yardage = 

        # hole_1_par = 
        # hole_1_yardage = 
        # hole_1_index = 

        # hole_2_par = 
        # hole_2_yardage = 
        # hole_2_index = 

        # hole_3_par =
        # hole_3_index = 

        # hole_4_par = 
        # hole_4_yardage =
        # hole_4_index =

        # hole_5_par = 
        # hole_5_yardage = 
        # hole_5_index = 

        # hole_6_par = 
        # hole_6_yardage = 
        # hole_6_index = 

        # hole_7_par = 
        # hole_7_yardage = 
        # hole_7_index =

        # hole_8_par 
        # hole_8_yardage 
        # hole_8_index

        # hole_9_par 
        # hole_9_yardage 
        # hole_9_index

        # hole_10_par
        # hole_10_yardage 
        # hole_10_index 

        # hole_11_par 
        # hole_11_yardage 
        # hole_11_index 

        # hole_12_par
        # hole_12_yardage 
        # hole_12_index = 

        # hole_13_par =
        # hole_13_yardage = 
        # hole_13_index = 

        # hole_14_par = 
        # hole_14_yardage = 
        # hole_14_index = 

        # hole_15_par = 
        # hole_15_yardage = 
        # hole_15_index = 

        # hole_16_par = 
        # hole_16_yardage 
        # hole_16_index 

        # hole_17_par  
        # hole_17_yardage 
        # hole_17_index  

        # hole_18_par  
        # hole_18_yardage  
        # hole_18_index 


print(add_tee(premier))