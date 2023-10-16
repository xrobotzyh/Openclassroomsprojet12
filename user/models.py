from enum import Enum

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class DepartmentChoice(Enum):
        sales = "sales"
        support = "support"
        management = "management"

    phone = models.CharField(max_length=12)
    department = models.CharField(max_length=18,
                                  choices=[(choice.name, choice.value) for choice in DepartmentChoice])

    def is_sales(self):
        return self.department == 'sales'

    def is_support(self):
        return self.department == 'support'

    def is_management(self):
        return self.department == 'management'
