from django.contrib import admin
from user.models import User
from contact.models import Client
from contrat.models import Contract
from event.models import Event

# Register your models here.
admin.site.register((User, Client, Contract, Event))
