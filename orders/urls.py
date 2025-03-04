from django.urls import path
from .views import OrderListView, CreateOrderView

urlpatterns = [
    path('', OrderListView.as_view(), name='order_list'),
    path('create/', CreateOrderView.as_view(), name='create_order'),
]
