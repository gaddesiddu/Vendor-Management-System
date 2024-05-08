from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Vendor
from .serializers import VendorSerializer

class VendorCreate(generics.CreateAPIView):
   
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class VendorListView(generics.ListAPIView):

    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class VendorRetrieveView(generics.RetrieveAPIView):
    
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    lookup_url_kwarg = 'vendor_id'

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

class VendorUpdate(APIView):
   
    def put(self, request, vendor_id):
        try:
            vendor = Vendor.objects.get(pk=vendor_id)
        except Vendor.DoesNotExist:
            return Response({"error": "Vendor not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = VendorSerializer(vendor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VendorDelete(APIView):
    
    def delete(self, request, vendor_id):
        try:
            vendor = Vendor.objects.get(pk=vendor_id)
        except Vendor.DoesNotExist:
            return Response({"error": "Vendor not found"}, status=status.HTTP_404_NOT_FOUND)
        vendor.delete()
        return Response({"message": "Vendor deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
