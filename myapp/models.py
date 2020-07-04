from django.db import models

class User(models.Model):
    id = models.CharField(max_length=100, null = False, primary_key = True)
    real_name = models.CharField(max_length=200)
    tz = models.CharField(max_length=200)


class ActivityPeriod(models.Model):
    start_time = models.CharField(max_length=200)
    end_time = models.CharField(max_length=200)
