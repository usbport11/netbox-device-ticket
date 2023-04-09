from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.urls import reverse

from netbox.models import NetBoxModel
from utilities.choices import ChoiceSet

class DeviceTicketStatusTypeChoices(ChoiceSet):
    key = 'DeviceTicket.status'

    CHOICES = [
        ('open', 'Open', 'green'),
        ('hold', 'Hold', 'orange'),
        ('closed', 'Closed', 'indigo'),
        ('reject', 'Reject', 'red'),
    ]

class DeviceTicket(NetBoxModel):
    name = models.CharField(
        max_length=100,
    )
    summary = models.CharField(
        max_length=200,
    )
    status = models.CharField(
        max_length=30,
        choices=DeviceTicketStatusTypeChoices
    )
    device = models.ForeignKey(
        to='dcim.Device',
        on_delete=models.CASCADE,
        related_name='+',
        default=None
    )
    comments = models.TextField(
        blank=True
    )

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('plugins:netbox_device_tickets:deviceticket', args=[self.pk])

    def get_status_color(self):
        return DeviceTicketStatusTypeChoices.colors.get(self.status)
