from django.db import models
from technicians.models import Technician
from jobs.models import Job


# Create your models here.
class PartOrder(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, default=None)
    part_number = models.CharField(max_length=40, default='none')
    part_type = models.CharField(max_length=40, default='none')
    reason_needed = models.TextField(max_length=250, default='none')
    date_ordered = models.DateTimeField(auto_now=True)
    ordered_by = models.ForeignKey(Technician, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return str(self.id)
