from django.urls import path

from . import views
from order_parts import views as order_part_views
from jobs import views as jobs_views
from technicians import views as technician_views

urlpatterns = [
    path('', views.index, name='index'),
    path('', order_part_views.IndexView.as_view(), name='PartsOrderedIndex'),
    path('', jobs_views.IndexView.as_view(), name='jobIndexView'),
    path('', technician_views.IndexView.as_view(), name='technicianIndexView'),
]
