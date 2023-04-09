import django_tables2 as tables
from netbox.tables import NetBoxTable, ChoiceFieldColumn
from .models import DeviceTicket

class DeviceTicketTable(NetBoxTable):
    name = tables.Column(
        linkify=True
    )
    status = ChoiceFieldColumn()

    class Meta(NetBoxTable.Meta):
        model = DeviceTicket
        fields = ('pk', 'id', 'name', 'device', 'summay', 'status', 'actions')
        default_columns = ('name', 'device', 'summary', 'status', 'actions')
