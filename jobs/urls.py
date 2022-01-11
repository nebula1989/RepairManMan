from django.urls import path

from . import views
from jobs.views import IndexView, JobArchiveView, JobUpdateView, JobDeleteView

urlpatterns = [
    path('', IndexView.as_view(), name='jobIndexView'),
    path('jobForm', views.job_form, name='job_form'),
    path('detail/<int:job_id>/', views.detail, name='detail_job'),
    path('<pk>/update', JobUpdateView.as_view(), name='job_update'),
    path('today/', JobArchiveView.as_view(), name='recent_jobs'),
    path('<pk>/delete/', JobDeleteView.as_view(), name='delete_job'),
]
