from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Vendor
from .serializers import VendorPerformanceSerializer


class VendorPerformance(viewsets.ReadOnlyModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorPerformanceSerializer

    def list(self, request):
        vendors = self.get_queryset()
        performance_data = []

        for vendor in vendors:
            # Calculate and serialize performance metrics for each vendor
            performance_metrics = {
                'vendor_id': vendor.id,
                # Using quality_rating_avg instead of quality_rating
                'on_time_delivery_rate': vendor.on_time_delivery_rate,
                'quality_rating': vendor.quality_rating_avg,
                'response_time': vendor.average_response_time,
                'fulfilment_rate': vendor.fulfillment_rate
            }
            performance_data.append(performance_metrics)

        return Response(performance_data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        vendor = self.get_object()
        # Calculate and serialize performance metrics for the specified vendor
        performance_metrics = {
            'vendor_id': vendor.id,
            # Using quality_rating_avg instead of quality_rating
            'on_time_delivery_rate': vendor.on_time_delivery_rate,
            'quality_rating': vendor.quality_rating_avg,
            'response_time': vendor.average_response_time,
            'fulfilment_rate': vendor.fulfillment_rate
        }
        return Response(performance_metrics, status=status.HTTP_200_OK)
