from django.db import models


# Create your models here.
class OrderPart(models.Model):
    work_order = models.IntegerField()
    part_number = models.CharField(max_length=40, default='none')
    part_type = models.CharField(max_length=40, default='none')
    reason_needed = models.TextField(max_length=250, default='none')

    def __str__(self):
        str_output = "\nWork Order: %d \n" \
                 "Part Number: %s \n" \
                 "Part Type: %s\n" \
                 "Reason Needed: %s" % (self.work_order, self.part_number, self.part_type, self.reason_needed)
        return str_output
