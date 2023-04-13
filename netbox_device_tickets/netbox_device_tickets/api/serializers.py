from rest_framework import serializers

from dcim.api.nested_serializers import NestedDeviceSerializer
from netbox.api.serializers import NetBoxModelSerializer, WritableNestedSerializer
from ..models import DeviceTicket

#
# Nested serializers
#

class NestedDeviceTicketSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_device_tickets-api:deviceticket-detail'
    )

    class Meta:
        model = DeviceTicket
        fields = ('id', 'url', 'display', 'name')
#
# Regular serializers
#

class DeviceTicketSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_device_tickets-api:deviceticket-detail'
    )

    device = NestedDeviceSerializer()

    class Meta:
        model = DeviceTicket
        fields = (
            'id', 'url', 'display', 'name', 'description', 'status', 'device', 'creator', 'executor', 'start', 'end', 'comments', 'tags', 'custom_fields', 
            'created', 'last_updated',
        )
