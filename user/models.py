from enum import Enum

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class DepartmentChoice(Enum):
        sales = "sales"
        support = "support"
        management = "management"

    telephone = models.CharField(max_length=12)
    department = models.CharField(max_length=18,
                                  choices=[(choice.name, choice.value) for choice in DepartmentChoice])
