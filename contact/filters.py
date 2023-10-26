from django_filters import rest_framework as filters

from contrat.models import Client


class ContactFilter(filters.FilterSet):
    """
      filter the clients list by their first name, last name, company name
      ordering the clients list by their first name, last name, phone number
      """
    ordering = filters.OrderingFilter(
        fields=(('first_name', 'ordering by first name'), ('last_name', 'ordering by last name'),
                ))

    class Meta:
        model = Client
        fields = {
            'first_name': ['icontains'],
            'last_name': ['icontains'],
            'company_name': ['icontains'],
        }
