import django_tables2 as tables
from netbox.tables import NetBoxTable, ChoiceFieldColumn
from .models import DeviceTicket

class DeviceTicketTable(NetBoxTable):
    name = tables.Column(
        linkify=True
    )
    device = tables.Column(
        linkify=True
    )
    status = ChoiceFieldColumn()

    class Meta(NetBoxTable.Meta):
        model = DeviceTicket
        fields = ('pk', 'id', 'name', 'device', 'description', 'status', 'creator', 'executor', 'start', 'end', 'actions')
        default_columns = ('name', 'device', 'description', 'status', 'creator', 'executor', 'start', 'end', 'actions')
