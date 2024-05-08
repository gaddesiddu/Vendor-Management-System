from django.db import models

class PurchaseOrder(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('SHIPPED', 'Shipped'),
        ('DELIVERED', 'Delivered'),
    ]

    po_number = models.CharField(max_length=100)
    vendor = models.ForeignKey('vendor.Vendor', on_delete=models.CASCADE)
    order_date = models.DateField()
    delivery_date = models.DateField()
    items = models.TextField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    quality_rating = models.FloatField(default=0.0)
    issue_date = models.DateField(auto_now_add=True)
    acknowledgement_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.po_number
