from extras.plugins import PluginMenuButton, PluginMenuItem
from utilities.choices import ButtonColorChoices


deviceticket_buttons = [
    PluginMenuButton(
        link='plugins:netbox_device_tickets:deviceticket_add',
        title='Add',
        icon_class='mdi mdi-plus-thick',
        color=ButtonColorChoices.GREEN
    )
]

menu_items = (
    PluginMenuItem(
        link='plugins:netbox_device_tickets:deviceticket_list',
        link_text='Device Tickets',
        buttons=deviceticket_buttons
    ),
)
