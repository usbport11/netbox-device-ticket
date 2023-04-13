from netbox.views import generic
from django.db.models import Count
from . import filtersets, forms, models, tables

class DeviceTicketView(generic.ObjectView):
    queryset = models.DeviceTicket.objects.all()

class DeviceTicketListView(generic.ObjectListView):
    queryset = models.DeviceTicket.objects.all()
    table = tables.DeviceTicketTable
    filterset = filtersets.DeviceTicketFilterSet
    filterset_form = forms.DeviceTicketFilterForm

class DeviceTicketEditView(generic.ObjectEditView):
    queryset = models.DeviceTicket.objects.all()
    form = forms.DeviceTicketForm

class DeviceTicketDeleteView(generic.ObjectDeleteView):
    queryset = models.DeviceTicket.objects.all()
