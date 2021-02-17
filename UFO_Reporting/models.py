from django.db import models


class Ufo(models.Model):
    row_string = models.CharField(max_length=100)



class UfoReport(models.Model):
    Date = models.DateTimeField()
    City = models.CharField(max_length=256)
    State = models.CharField(max_length=256)
    Shape = models.CharField(max_length=256)
    Duration = models.CharField(max_length=256)
    Summary = models.CharField(max_length=256)
    Posted = models.DateTimeField()

    def __str__(self):
        return self.Duration
