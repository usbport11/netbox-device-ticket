from netbox.api.viewsets import NetBoxModelViewSet

from .. import models, filtersets
from .serializers import DeviceTicketSerializer

class DeviceTicketViewSet(NetBoxModelViewSet):
    queryset = models.DeviceTicket.objects.prefetch_related('tags')
    serializer_class = DeviceTicketSerializer
    filterset_class = filtersets.DeviceTicketFilterSet
