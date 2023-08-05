from django.db import models
from golf_trip.models import Trip_TeeTime, Trip_Golfer


    

class Round_Score(models.Model):
    tee_time = models.ForeignKey(Trip_TeeTime, on_delete=models.PROTECT)
    round_golfer = models.CharField(max_length=255)
    golfer_pk = models.ForeignKey(Trip_Golfer, on_delete=models.PROTECT)
    golfer_index = models.DecimalField(decimal_places=1, max_digits=3)
    hole_1_score = models.IntegerField()
    hole_2_score = models.IntegerField()
    hole_3_score = models.IntegerField()
    hole_4_score = models.IntegerField()
    hole_5_score = models.IntegerField()
    hole_6_score = models.IntegerField()
    hole_7_score = models.IntegerField()
    hole_8_score = models.IntegerField()
    hole_9_score = models.IntegerField()
    hole_10_score = models.IntegerField()
    hole_11_score = models.IntegerField()
    hole_12_score = models.IntegerField()
    hole_13_score = models.IntegerField()
    hole_14_score = models.IntegerField()
    hole_15_score = models.IntegerField()
    hole_16_score = models.IntegerField()
    hole_17_score = models.IntegerField()
    hole_18_score = models.IntegerField()
    total_score = models.IntegerField(default=0)
    net_score = models.IntegerField(default=0)

    def __str__(self):
        return "{}_{}".format(self.round_golfer, self.tee_time)
    

class Net_Round_Score(models.Model):
    tee_time = models.ForeignKey(Trip_TeeTime, on_delete=models.PROTECT)
    round_golfer = models.CharField(max_length=255)
    golfer_pk = models.ForeignKey(Trip_Golfer, on_delete=models.PROTECT)
    hole_1_score = models.IntegerField()
    hole_2_score = models.IntegerField()
    hole_3_score = models.IntegerField()
    hole_4_score = models.IntegerField()
    hole_5_score = models.IntegerField()
    hole_6_score = models.IntegerField()
    hole_7_score = models.IntegerField()
    hole_8_score = models.IntegerField()
    hole_9_score = models.IntegerField()
    hole_10_score = models.IntegerField()
    hole_11_score = models.IntegerField()
    hole_12_score = models.IntegerField()
    hole_13_score = models.IntegerField()
    hole_14_score = models.IntegerField()
    hole_15_score = models.IntegerField()
    hole_16_score = models.IntegerField()
    hole_17_score = models.IntegerField()
    hole_18_score = models.IntegerField()
    total_score = models.IntegerField()
    net_score = models.IntegerField()

    def __str__(self):
        return "{}_{}".format(self.round_golfer, self.tee_time)
    

class Par3_Round_Score(models.Model):
    tee_time = models.ForeignKey(Trip_TeeTime, on_delete=models.PROTECT)
    round_golfer = models.CharField(max_length=255)
    golfer_pk = models.ForeignKey(Trip_Golfer, on_delete=models.PROTECT)
    golfer_index = models.DecimalField(decimal_places=1, max_digits=3)
    hole_1_score = models.IntegerField()
    hole_2_score = models.IntegerField()
    hole_3_score = models.IntegerField()
    hole_4_score = models.IntegerField()
    hole_5_score = models.IntegerField()
    hole_6_score = models.IntegerField()
    hole_7_score = models.IntegerField()
    hole_8_score = models.IntegerField()
    hole_9_score = models.IntegerField()
    total_score = models.IntegerField(default=0)
    net_score = models.IntegerField(default=0)

    def __str__(self):
        return "{}_{}".format(self.round_golfer, self.tee_time)
    

class Par3_Net_Round_Score(models.Model):
    tee_time = models.ForeignKey(Trip_TeeTime, on_delete=models.PROTECT)
    round_golfer = models.CharField(max_length=255)
    golfer_pk = models.ForeignKey(Trip_Golfer, on_delete=models.PROTECT)
    hole_1_score = models.IntegerField()
    hole_2_score = models.IntegerField()
    hole_3_score = models.IntegerField()
    hole_4_score = models.IntegerField()
    hole_5_score = models.IntegerField()
    hole_6_score = models.IntegerField()
    hole_7_score = models.IntegerField()
    hole_8_score = models.IntegerField()
    hole_9_score = models.IntegerField()
    total_score = models.IntegerField()
    net_score = models.IntegerField()

    def __str__(self):
        return "{}_{}".format(self.round_golfer, self.tee_time)


