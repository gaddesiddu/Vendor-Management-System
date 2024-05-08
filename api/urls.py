from performance.views import VendorPerformance
from django.urls import path, include

from vendor.views import VendorListView, VendorCreate, VendorDelete, VendorRetrieveView, VendorUpdate
urlpatterns = [
    # Other URL patterns
    path('vendors/', include([
        # Other vendor-related URL patterns
        path('performance/', VendorPerformance.as_view({'get': 'list'}), name='vendor-performance'),
    ])),
]