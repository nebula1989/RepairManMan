from django.urls import path

from . import views
from order_parts.views import PartsOrdersListView

urlpatterns = [
    path('', views.index, name='index'),
    path('success/', PartsOrdersListView.as_view(), name='success')
]
