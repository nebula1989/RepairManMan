from django.db import models
from technicians.models import Technician


# Create your models here.
class Job(models.Model):
    status_choices = (
        ('FV', 'First Visit / Troubleshoot'),
        ('AWP', 'Awaiting Part'),
        ('INP', 'In Progress'),
        ('C', 'Completed')
    )
    status = models.CharField(choices=status_choices, max_length=50)
    service_notes = models.TextField(max_length=250, default="No Notes Provided")
    assigned_technician = models.ForeignKey(Technician, models.DO_NOTHING)

    def __str__(self):
        return str(self.id)
