from django.urls import path
from purchase_orders.views import PurchaseOrderViewSet

urlpatterns = [
    path('purchase_orders/', PurchaseOrderViewSet.as_view({
        'get': 'list',
        'post': 'create'
    }), name='purchase-order-list'),
    path('purchase_orders/<int:pk>/', PurchaseOrderViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    }), name='purchase-order-detail'),
    path('purchase_orders/<int:pk>/acknowledge/', PurchaseOrderViewSet.as_view({
        'post': 'acknowledge'
    }), name='purchase-order-acknowledge'),
]
