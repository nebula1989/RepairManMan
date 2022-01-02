from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.http import Http404
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.views.generic.dates import TodayArchiveView
from .forms import PartOrderingForm
from .models import OrderPart


# Create your views here.
def part_order_form(request):
    context = {}
    
    # create form object
    form = PartOrderingForm(request.POST or None, request.FILES or None)
    
    # validate form
    if form.is_valid():
        form.save()
    
    context['form'] = form
    return render(request, 'order_parts/order_parts.html', context)


class IndexView(ListView):
    model = OrderPart
    context_object_name = 'latest_partsordered_list'
    template_name = 'order_parts/index.html'

    def get_queryset(self):
        """Return the last ten ordered parts."""
        return OrderPart.objects.filter(
            date_ordered__lte=timezone.now()
        ).order_by('date_ordered')[:10]


def detail(request, part_order_id):
    try:
        part_order = OrderPart.objects.get(pk=part_order_id)
    except OrderPart.DoesNotExist:
        raise Http404("Part Order does not exist")
    return render(request, 'order_parts/detail.html',
                  {'part_order': part_order})


class PartsOrdersArchiveView(TodayArchiveView):
    queryset = OrderPart.objects.all()
    context_object_name = 'latest_partsordered_list'
    date_field = "date_ordered"
    template_name = 'order_parts/index.html'

