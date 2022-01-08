from django.forms import ModelForm
from order_parts.models import PartOrder


class PartOrderingForm(ModelForm):
    class Meta:
        model = PartOrder
        fields = "__all__"
