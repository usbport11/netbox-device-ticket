from netbox.filtersets import NetBoxModelFilterSet
from .models import DeviceTicket


class DeviceTicketFilterSet(NetBoxModelFilterSet):
    class Meta:
        model = DeviceTicket
        fields = ('id', 'name', 'description', 'status', 'device', 'creator', 'executor', 'start', 'end', 'comments')

    def search(self, queryset, name, value):
        return queryset.filter(name__icontains=value)
