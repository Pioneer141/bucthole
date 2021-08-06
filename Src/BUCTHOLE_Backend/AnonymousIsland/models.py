from django.db import models


class BLOCK(models.Model):
    ID = models.IntegerField()
    LEFT_UP_LNG = models.CharField(max_length=255)
    LEFT_UP_LAT = models.CharField(max_length=255)
    RIGHT_UP_LNG = models.CharField(max_length=255)
    RIGHT_UP_LAT = models.CharField(max_length=255)
    RIGHT_DOWN_LNG = models.CharField(max_length=255)
    RIGHT_DOWN_LAT = models.CharField(max_length=255)
    LEFT_DOWN_LNG = models.CharField(max_length=255)
    LEFT_DOWN_LAT = models.CharField(max_length=255)
    CENTER_LNG = models.CharField(max_length=255)
    CENTER_LAT = models.CharField(max_length=255)



class NOTE(models.Model):
    NOTEID = models.AutoField(primary_key=True)
    BLOCKID = models.IntegerField()
    NOTEDATA = models.CharField(max_length=255)
