from django.urls import path

from . import views
from order_parts.views import PartsOrdersListView, PartsOrdersArchiveView

urlpatterns = [
    path('', views.part_order_form, name='part_order_form'),
    path('AllPartOrders/', PartsOrdersListView.as_view(), name='all_part_orders'),
    path('today/', PartsOrdersArchiveView.as_view(), name='todays_part_orders'),
]
