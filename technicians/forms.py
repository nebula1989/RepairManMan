from django.forms import ModelForm
from technicians.models import Technician


class TechnicianForm(ModelForm):
    class Meta:
        model = Technician
        fields = "__all__"
