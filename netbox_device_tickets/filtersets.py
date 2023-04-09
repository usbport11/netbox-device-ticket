from netbox.filtersets import NetBoxModelFilterSet
from .models import DeviceTicket


class DeviceTicketFilterSet(NetBoxModelFilterSet):
    class Meta:
        model = DeviceTicket
        fields = ('id', 'name', 'summary', 'status', 'device', 'comments')

    def search(self, queryset, name, value):
        return queryset.filter(name__icontains=value)
