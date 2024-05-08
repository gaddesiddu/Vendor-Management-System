from django.urls import path
from .import views


urlpatterns = [
    path('vendors/post/', views.VendorCreate.as_view(), name='vendorcreate'),
    path('vendors/get/', views.VendorListView.as_view(), name='vendorlistview'),
    path('vendors/get/<int:vendor_id>/', views.VendorRetrieveView.as_view(), name='vendoridview'),
    path('vendors/put/<int:vendor_id>/', views.VendorUpdate.as_view(), name='vendoridupdate'),
    path('vendors/delete/<int:vendor_id>/', views.VendorDelete.as_view(), name='vendoriddelete'),
    
]
