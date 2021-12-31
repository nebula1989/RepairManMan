from django.db import models


# Create your models here.
class OrderParts(models.Model):
    work_order = models.IntegerField()
    part_number = models.CharField(max_length=40, default='none')

    def __str__(self):
        output = "\nWork Order: %d \n" \
                 "Part Number: %s" % (self.work_order, self.part_number)
        return output
