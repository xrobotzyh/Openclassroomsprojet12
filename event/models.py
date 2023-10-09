from django.db import models

from contact.models import Client
from contrat.models import Contract
from user.models import User


class Event(models.Model):
    event_id = models.UUIDField(unique=True, primary_key=True)
    contrat_id = models.ForeignKey(to=Contract, on_delete=models.CASCADE, related_name='contrat_id_event')
    client_name = models.ForeignKey(to=Client, on_delete=models.CASCADE)
    client_contact = models.ForeignKey(to=Contract, on_delete=models.CASCADE, related_name='client_contact_event')
    support_contact = models.ForeignKey(to=User, on_delete=models.CASCADE)
    attendees = models.PositiveSmallIntegerField()
    location = models.TextField(max_length=512)
    notes = models.TextField(max_length=512)
    event_start_at = models.DateTimeField(auto_now_add=True, null=False)
    event_update_at = models.DateTimeField(auto_now=True, null=True)
    event_end_at = models.DateTimeField(null=True)
