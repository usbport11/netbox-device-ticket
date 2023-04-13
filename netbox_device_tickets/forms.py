from django import forms
from netbox.forms import NetBoxModelForm, NetBoxModelFilterSetForm
from utilities.forms import DateTimePicker, DynamicModelChoiceField
from dcim.models import Device
from .models import DeviceTicket, DeviceTicketStatusTypeChoices

class DeviceTicketForm(NetBoxModelForm):
    device = DynamicModelChoiceField(
        queryset=Device.objects.all()
    )

    class Meta:
        model = DeviceTicket
        fields = ('name', 'description', 'status', 'device', 'creator', 'executor', 'start', 'end', 'comments', 'tags')
        widgets = {
            'start': DateTimePicker(),
            'end': DateTimePicker()
        }

class DeviceTicketFilterForm(NetBoxModelFilterSetForm):
    model = DeviceTicket

    name = forms.CharField(
        required=False
    )

    summary = forms.CharField(
        required=False
    )

    device = forms.ModelMultipleChoiceField(
        queryset=Device.objects.all(),
        required=False
    )

    status = forms.MultipleChoiceField(
        choices=DeviceTicketStatusTypeChoices,
        required=False
    )

    creator = forms.CharField(
        required=False
    )

    executor = forms.CharField(
        required=False
    )

    start = forms.CharField(
        required=False
    )

    end = forms.CharField(
        required=False
    )
