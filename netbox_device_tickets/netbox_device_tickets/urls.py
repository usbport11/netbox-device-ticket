from django.urls import path
from netbox.views.generic import ObjectChangeLogView
from . import models, views

urlpatterns = (
    path('device-tickets/', views.DeviceTicketListView.as_view(), name='deviceticket_list'),
    path('device-tickets/add/', views.DeviceTicketEditView.as_view(), name='deviceticket_add'),
    path('device-tickets/<int:pk>/', views.DeviceTicketView.as_view(), name='deviceticket'),
    path('device-tickets/<int:pk>/edit/', views.DeviceTicketEditView.as_view(), name='deviceticket_edit'),
    path('device-tickets/<int:pk>/delete/', views.DeviceTicketDeleteView.as_view(), name='deviceticket_delete'),
    path('device-tickets/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='deviceticket_changelog', kwargs={
        'model': models.DeviceTicket
    }),
)
