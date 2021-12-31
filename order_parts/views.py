from django.shortcuts import render
from django.views.generic import ListView
from .forms import PartOrderingForm
from .models import OrderParts


# Create your views here.
def index(request):
    context = {}
    
    # create form object
    form = PartOrderingForm(request.POST or None, request.FILES or None)
    
    # validate form
    if form.is_valid():
        form.save()
    
    context['form'] = form
    return render(request, 'order_parts/order_parts.html', context)


class PartsOrdersListView(ListView):
    model = OrderParts

    template_name = 'order_parts/parts_successfully_ordered.html'
