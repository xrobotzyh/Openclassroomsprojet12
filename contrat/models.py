import uuid
from enum import Enum

from django.db import models

from contact.models import Client


class Contract(models.Model):
    class ContractStatus(Enum):
        sign = 'signed'
        not_sign = 'not signed'

    id = models.UUIDField(unique=True, primary_key=True, default=uuid.uuid4)
    client = models.ForeignKey(to=Client, on_delete=models.CASCADE, related_name='client')
    quotation = models.DecimalField(decimal_places=2, max_digits=32)
    paid = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    status = models.CharField(max_length=10,
                              choices=[(choice.name, choice.value) for choice in ContractStatus])
