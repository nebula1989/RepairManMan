from django.forms import ModelForm
from order_parts.models import OrderParts


class PartOrderingForm(ModelForm):
    class Meta:
        model = OrderParts
        fields = "__all__"
