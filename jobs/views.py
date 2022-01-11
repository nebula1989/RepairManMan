from django.http import Http404
from django.utils import timezone
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.dates import TodayArchiveView
from django.views.generic.edit import UpdateView, DeleteView

from .forms import JobForm
from .models import Job


# Create your views here.
def job_form(request):
    context = {}

    # create form object
    form = JobForm(request.POST or None, request.FILES or None)

    # validate form
    if form.is_valid():
        form.save()

    context['form'] = form
    return render(request, 'jobs/jobs.html', context)


class IndexView(ListView):
    model = Job
    context_object_name = "latest_jobs_created_list"
    template_name = 'jobs/index.html'


def detail(request, job_id):
    try:
        job = Job.objects.get(pk=job_id)
    except Job.DoesNotExist:
        raise Http404("Job does not exist")
    return render(request, 'jobs/detail.html',
                  {'job': job})


class JobUpdateView(UpdateView):
    model = Job
    fields = '__all__'
    template_name = 'jobs/job_update_form.html'
    success_url = '/jobs'


class JobDeleteView(DeleteView):
    model = Job
    success_url = reverse_lazy('jobIndexView')


class JobArchiveView(TodayArchiveView):
    queryset = Job.objects.all()
    context_object_name = 'latest_jobs_list'
    template_name = 'jobs/index.html'


