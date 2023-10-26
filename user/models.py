from enum import Enum

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
      a user models heritage the abstractuser, add department information phone number
      check methode to check is the user is belongs to sales or support or management department
    """
    class DepartmentChoice(Enum):
        sales = "sales"
        support = "support"
        management = "management"

    phone = models.CharField(max_length=12)
    department = models.CharField(max_length=18,
                                  choices=[(choice.name, choice.value) for choice in DepartmentChoice])

    def is_sales(self):
        return self.department == User.DepartmentChoice.sales.value

    def is_support(self):
        return self.department == User.DepartmentChoice.support.value

    def is_management(self):
        return self.department == User.DepartmentChoice.management.value
