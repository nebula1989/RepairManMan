from django.utils import timezone
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.dates import TodayArchiveView
from django.views.generic.edit import UpdateView, DeleteView

from .forms import PartOrderingForm
from .models import PartOrder


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
    model = PartOrder
    context_object_name = 'latest_partsordered_list'
    template_name = 'order_parts/index.html'

    def get_queryset(self):
        """Return the last ten ordered parts."""
        return PartOrder.objects.filter(
            date_ordered__lte=timezone.now()
        ).order_by('date_ordered')[:10]


def detail(request, part_order_id):
    try:
        part_order = PartOrder.objects.get(pk=part_order_id)
    except PartOrder.DoesNotExist:
        raise Http404("Part Order does not exist")
    return render(request, 'order_parts/detail.html',
                  {'part_order': part_order})


class PartsOrdersUpdateView(UpdateView):
    model = PartOrder
    fields = '__all__'
    template_name = 'order_parts/order_parts_update_form.html'
    success_url = '/order_parts'


class PartsOrderDeleteView(DeleteView):
    model = PartOrder
    success_url = reverse_lazy('PartsOrderedIndex')


class PartsOrdersArchiveView(TodayArchiveView):
    queryset = PartOrder.objects.all()
    context_object_name = 'latest_partsordered_list'
    date_field = "date_ordered"
    template_name = 'order_parts/index.html'


def error_404_view(request, exception):
    data = {"THING": "stuffs"}
    return render(request, '404.html', data)
