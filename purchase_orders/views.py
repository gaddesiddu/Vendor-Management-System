from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import PurchaseOrder
from .serializers import PurchaseOrderSerializer
from django.shortcuts import get_object_or_404
from django.utils import timezone

class PurchaseOrderViewSet(viewsets.ViewSet):
    def create(self, request):
        serializer = PurchaseOrderSerializer(data=request.data)
        if serializer.is_valid():  # Call is_valid() first
            serializer.save()  # Then save the serializer
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



    def list(self, request):
        queryset = PurchaseOrder.objects.all()
        serializer = PurchaseOrderSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        purchase_order = get_object_or_404(PurchaseOrder, pk=pk)
        serializer = PurchaseOrderSerializer(purchase_order)
        return Response(serializer.data)

    def update(self, request, pk=None):
        purchase_order = get_object_or_404(PurchaseOrder, pk=pk)
        serializer = PurchaseOrderSerializer(instance=purchase_order, data=request.data)

        # Check if data is valid
            # If valid, save the data
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response(serializer.data)
        

    def destroy(self, request, pk=None):
        purchase_order = get_object_or_404(PurchaseOrder, pk=pk)
        purchase_order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=True, methods=['post'])
    def acknowledge(self, request, pk=None):
        purchase_order = get_object_or_404(PurchaseOrder, pk=pk)

        if not purchase_order.acknowledgement_date:
            try:
                purchase_order.acknowledgement_date = timezone.now()
                purchase_order.save()
            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        purchase_order_detail = {
            'purchase_order': purchase_order.po_number,
            'vendor': purchase_order.vendor.name,
            'order_date': purchase_order.order_date,
            'delivery_date': purchase_order.delivery_date,
            'items': purchase_order.items,
            'quantity': purchase_order.quantity,
            'status': purchase_order.status,
            'quality_rating': purchase_order.quality_rating,
            'issue_date': purchase_order.issue_date,
            'acknowledgement_date': purchase_order.acknowledgement_date
        }

        return Response(purchase_order_detail)
