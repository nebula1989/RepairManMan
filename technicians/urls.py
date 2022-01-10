from django.urls import path

from . import views
from technicians.views import IndexView, TechnicianArchiveView, TechnicianUpdateView, TechnicianDeleteView

urlpatterns = [
    path('', IndexView.as_view(), name='technicianIndexView'),
    path('technicianForm', views.technician_form, name='technician_form'),
    path('detail/<int:technician_id>/', views.detail, name='detail_technician'),
    path('<pk>/update', TechnicianUpdateView.as_view(), name='technician_update'),
    path('today/', TechnicianArchiveView.as_view(), name='recent_techs'),
    path('<pk>/delete/', TechnicianDeleteView.as_view(), name='delete_technician'),
]
