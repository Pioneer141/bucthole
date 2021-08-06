from django.db import models


class USER(models.Model):
    UID = models.AutoField(primary_key=True)
    UNAME = models.CharField(max_length=255)
    UPASSWORD = models.CharField(max_length=255)
    UCOOKIESLIST = models.CharField(max_length=255)
    UROLE = models.CharField(max_length=255)

class NOTE(models.Model):
    NID = models.AutoField(primary_key=True)
    UCOOKIE = models.CharField(max_length=255)
    TIME = models.CharField(max_length=255)
    CONTENT = models.CharField(max_length=255)
