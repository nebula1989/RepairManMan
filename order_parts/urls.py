from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('success', views.parts_successfully_ordered, name='parts_successfully_ordered')
]
