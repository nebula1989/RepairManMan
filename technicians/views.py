from django.http import Http404
from django.utils import timezone
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.dates import TodayArchiveView
from django.views.generic.edit import UpdateView, DeleteView

from .forms import TechnicianForm
from .models import Technician


# Create your views here.
def technician_form(request):
    context = {}

    # create form object
    form = TechnicianForm(request.POST or None, request.FILES or None)

    # validate form
    if form.is_valid():
        form.save()

    context['form'] = form
    return render(request, 'technicians/technicians.html', context)


class IndexView(ListView):
    model = Technician
    context_object_name = "latest_techs_created_list"
    template_name = 'technicians/index.html'


def detail(request, technician_id):
    try:
        technician = Technician.objects.get(pk=technician_id)
    except Technician.DoesNotExist:
        raise Http404("Technician does not exist")
    return render(request, 'technicians/detail.html',
                  {'technician': technician})


class TechnicianUpdateView(UpdateView):
    model = Technician
    fields = '__all__'
    template_name = 'technicians/technician_update_form.html'
    success_url = '/technicians'


class TechnicianDeleteView(DeleteView):
    model = Technician
    success_url = reverse_lazy('technicianIndexView')


class TechnicianArchiveView(TodayArchiveView):
    queryset = Technician.objects.all()
    context_object_name = 'latest_technician_list'
    template_name = 'technicians/index.html'


