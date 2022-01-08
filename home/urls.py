from django.urls import path

from . import views
from order_parts import views as order_part_views
from jobs import views as jobs_views

urlpatterns = [
    path('', views.index, name='index'),
    path('', order_part_views.IndexView.as_view(), name='PartsOrderedIndex'),
    path('', jobs_views.indexView, name='jobIndexView')
]
