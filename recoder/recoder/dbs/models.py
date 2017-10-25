from django.db import models


class Temperature(models.Model):
    temp_val = models.FloatField('temperature value')
    temp_date = models.DateTimeField('measurement date')
    mac_addr = models.CharField(max_length=17)

class Location(models.Model):
    location_id = models.IntegerField()
    location_nm = models.CharField(max_length=100)
    detail_nm = models.CharField(max_length=100)

class SettingInfo(models.Model):
    location_id = models.IntegerField()
    mac_addr = models.CharField(max_length=17)
    start_date = models.DateTimeField('measurement start date')
    end_date = models.DateTimeField('measurement end date')

