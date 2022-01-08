from django.http import Http404
from django.utils import timezone
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.dates import TodayArchiveView
from django.views.generic.edit import UpdateView, DeleteView


def indexView(request):
    return render(request, 'technicians/index.html')
