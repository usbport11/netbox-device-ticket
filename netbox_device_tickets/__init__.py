from extras.plugins import PluginConfig

class NetBoxDeviceTiketsConfig(PluginConfig):
    name = 'netbox_device_tickets'
    verbose_name = ' NetBox Device Tickets'
    description = 'Manage device service tickets'
    version = '0.1'
    base_url = 'device-tickets'
    min_version = '3.3.0'

config = NetBoxDeviceTiketsConfig
