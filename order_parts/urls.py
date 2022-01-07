from django.urls import path

from . import views
from order_parts.views import IndexView, PartsOrdersArchiveView, PartsOrdersUpdateView, PartsOrderDeleteView


urlpatterns = [
    path('', IndexView.as_view(), name='PartsOrderedIndex'),
    path('partsForm', views.part_order_form, name='part_order_form'),
    path('detail/<int:part_order_id>/', views.detail, name='detail'),
    path('<pk>/update', PartsOrdersUpdateView.as_view(), name='update'),
    path('today/', PartsOrdersArchiveView.as_view(), name='todays_part_orders'),
    path('<pk>/delete/', PartsOrderDeleteView.as_view(), name='delete'),
]
