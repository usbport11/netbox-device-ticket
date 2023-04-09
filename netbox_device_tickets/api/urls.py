from netbox.api.routers import NetBoxRouter
from . import views

app_name = 'netbox_device_tickets'

router = NetBoxRouter()
router.register('deviceticket', views.DeviceTicketViewSet)

urlpatterns = router.urls
