from django.db import models
from vendor.models import Vendor


# HistoricalPerformance models .
class VendorPerformance(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE,null=True, db_constraint=False)
    date = models.DateTimeField()
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()

    def __str__(self):
        return f'{self.vendor} - {self.date}'