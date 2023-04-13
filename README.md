## netbox_device_tickets

Manage device service tickets

Install steps:

0) cd netbox_device_tickets
1) systecmtl stop netbox netbox-rq
2) /opt/netbox/venv/bin/activate
3) nano /opt/netbox/netbox/netbox/configuration.py
  PLUGINS = ['netbox_device_tickets']
4) pip3 install .
5) /opt/netbox/netbox/manage.py migrate
6) deactivate
7) systemctl start netbox netbox-rq
