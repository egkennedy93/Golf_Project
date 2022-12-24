from django.contrib import admin
from Courses.models import Golf_Hole, Golf_Course, Golf_Tee, New_Course_Entry

# Register your models here.
admin.site.register(Golf_Hole)
admin.site.register(Golf_Course)
admin.site.register(Golf_Tee)
admin.site.register(New_Course_Entry)
