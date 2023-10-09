from datetime import datetime
from enum import Enum

from django.db import models

from contact.models import Client


class Contract(models.Model):
    class ContractStatus(Enum):
        sign = 'signed'
        not_sign = 'not signed'

    id = models.UUIDField(unique=True, primary_key=True)
    client = models.ForeignKey(to=Client, on_delete=models.CASCADE, related_name='client')
    client_from = models.ForeignKey(to=Client, on_delete=models.CASCADE)
    # client_from = models.ForeignKey(to=Client, on_delete=models.CASCADE, to_field='contact_user', default=1)
    name = models.CharField(max_length=256)
    quotation = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    status = models.CharField(max_length=10,
                              choices=[(choice.name, choice.value) for choice in ContractStatus])
