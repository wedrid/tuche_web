from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class Report(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    time = models.DateTimeField(default = timezone.now) #TODO cambiare fuso orario (timezone)
    lat = models.FloatField()
    lon = models.FloatField()
    vehicle_type = models.IntegerField()
    intensity_x = models.FloatField()
    intensity_y = models.FloatField()
    intensity_z = models.FloatField()

    def __str__(self):
        return "Report di: " + str(self.user) + " in " + str(self.lat) + ", " + str(self.lon)