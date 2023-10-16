import uuid

from django.db import models

from user.models import User


class Client(models.Model):
    id = models.UUIDField(unique=True, primary_key=True, default=uuid.uuid4)
    contact = models.ForeignKey(to=User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=12)
    company_name = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False)
