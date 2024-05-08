from rest_framework import serializers
from .models import PurchaseOrder



class PurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = '__all__'

    # Validates the quantity field
    def validate_quantity(self,value):
        if value <= 0:
            raise serializers.ValidationError('Quantity Cannot be less than 1')
        return value

    # Validates the status field
    
    # Validates the quality_rating field
    