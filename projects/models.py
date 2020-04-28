from django.db import models
from agendas.models import Agenda

class Project(models.Model):
    name = models.CharField(max_length=100)
    due_date_day = models.IntegerField(blank=True, null=True)
    date_date_month = models.IntegerField(blank=True, null=True)
    date_date_year = models.IntegerField(blank=True, null=True)
    estimated_time_hours = models.IntegerField(blank=True, null=True)
    estimated_time_mins = models.IntegerField(blank=True, null=True)
    agenda = models.ForeignKey(Agenda, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name


