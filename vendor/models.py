from django.db import models



class Vendor(models.Model):
    name = models.CharField(max_length=100)
    contact_details = models.TextField()
    address = models.TextField()
    vendor_code = models.CharField(max_length=50, unique=True)
    on_time_delivery_rate = models.FloatField(default=0.0, null=True)

    quality_rating_avg = models.FloatField(default=0.0, null=True)
    average_response_time = models.FloatField(default=0.0, null=True)
    fulfillment_rate = models.FloatField(default=0.0, null=True)

    def __str__(self):
        return self.name
