from django.shortcuts import render
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


class PartsOrdersListView(ListView):
    model = OrderPart
    template_name = 'order_parts/view_part_orders.html'


class PartsOrdersArchiveView(TodayArchiveView):
    queryset = OrderPart.objects.all()
    date_field = "date_ordered"
    template_name = 'order_parts/view_part_orders.html'

