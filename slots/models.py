from django.db import models
from tasks.models import Task

class Slot(models.Model):
    day = models.IntegerField()
    month = models.IntegerField()
    year = models.IntegerField()
    start_time_hours = models.IntegerField()
    start_time_mins = models.IntegerField()
    end_time_hours = models.IntegerField()
    end_time_mins = models.IntegerField()
    task = models.ForeignKey(Task, on_delete=models.DO_NOTHING)
    is_done = models.BooleanField(default=False)
    is_added = models.BooleanField(default=False)

    def __str__(self):
        return self.task.name + ' ' + self.is_done

