from django.db import models


# Create your models here.
class PartOrder(models.Model):
    work_order = models.IntegerField()
    part_number = models.CharField(max_length=40, default='none')
    part_type = models.CharField(max_length=40, default='none')
    reason_needed = models.TextField(max_length=250, default='none')
    date_ordered = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.id
