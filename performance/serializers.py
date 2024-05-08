# serializers.py

from rest_framework import serializers
from .models import VendorPerformance

class VendorPerformanceSerializer(serializers.ModelSerializer):
    on_time_delivery_rate = serializers.DecimalField(max_digits=5, decimal_places=2)
    quality_rating = serializers.DecimalField(max_digits=5, decimal_places=2)
    response_time = serializers.DurationField()
    fulfilment_rate = serializers.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        model = VendorPerformance
        fields = ['vendor_id', 'on_time_delivery_rate', 'quality_rating', 'response_time', 'fulfilment_rate']
