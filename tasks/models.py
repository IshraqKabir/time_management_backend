from django.db import models

from agendas.models import Agenda
from projects.models import Project
from objectives.models import Objective


repeat_type_choices = [
    ('D', 'Daily'),
    ('W', 'Weekly'),
    ('M', 'Monthly'),
]

class Task(models.Model):
    name = models.CharField(max_length=100)
    agenda = models.ForeignKey(Agenda, on_delete=models.CASCADE, blank=True, null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, blank=True, null=True)
    objective = models.ForeignKey(Objective, on_delete=models.CASCADE, blank=True, null=True)
    # pre_requisite = 
    # post_requisite =
    # total_required_time_to_finish = models.CharField(max_length=10) 
    total_time_done = models.CharField(max_length=10, default='0:0')
    importance_rating = models.IntegerField()
    repeat_type = models.CharField(max_length=5, choices=repeat_type_choices, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # print(kwargs)
        super().save(*args, **kwargs)