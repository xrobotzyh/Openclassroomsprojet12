from django_filters import rest_framework as filters

from contrat.models import Client


class ContactFilter(filters.FilterSet):
    first_name = filters.CharFilter(field_name='first_name', lookup_expr='icontains', label='first name')
    last_name = filters.CharFilter(field_name='last_name', lookup_expr='icontains', label='last_name')
    ordering = filters.OrderingFilter(
        fields=(('first_name', 'ordering by first name'), ('last_name', 'ordering by last name'),
                ('phone', 'ordering by phone number')
                ))

    class Meta:
        model = Client
        fields = ['first_name', 'last_name']


