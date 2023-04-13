from netbox.api.routers import NetBoxRouter
from . import views

app_name = 'netbox_device_tickets'

router = NetBoxRouter()
router.register('device-tickets', views.DeviceTicketViewSet)

urlpatterns = router.urls
