import uuid

from django.db import models

from contact.models import Client
from contrat.models import Contract
from user.models import User


class Event(models.Model):
    id = models.UUIDField(unique=True, primary_key=True, default=uuid.uuid4)
    contrat = models.ForeignKey(to=Contract, on_delete=models.CASCADE, related_name='contrat_id_event')
    client = models.ForeignKey(to=Client, on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True)
    attendees = models.PositiveSmallIntegerField()
    location = models.TextField(max_length=512)
    notes = models.TextField(max_length=512)
    starts_at = models.DateTimeField(auto_now_add=True, null=False)
    ends_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
