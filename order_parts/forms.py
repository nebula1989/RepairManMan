from django.forms import ModelForm
from order_parts.models import OrderPart


class PartOrderingForm(ModelForm):
    class Meta:
        model = OrderPart
        fields = "__all__"
