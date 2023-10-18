from django.db import models
from django.db.models import Q
from django_filters import rest_framework as filters

from contrat.models import Contract


class ContractFilter(filters.FilterSet):
    """
      filter the contracts list by their sign status, payment status(payment finished or not),quotation amount more than
      filter the contracts by contracts attached client's first name, last name
      """
    contract_status = filters.ChoiceFilter(field_name='status', choices=[(choice.name, choice.value) for choice in
                                                                         Contract.ContractStatus],
                                           label='Contract_Status')
    total_paid = filters.CharFilter(method='filter_total_paid', label='payment complete,true or false')
    quotation_more_than = filters.NumberFilter(field_name='quotation', lookup_expr='gt', label='quotation >')

    class Meta:
        model = Contract
        fields = {'client__first_name': ['icontains'],
                  'client__last_name': ['icontains'],
                  }

    def filter_total_paid(self, queryset, name, value):
        if value.lower() == 'true':
            return queryset.filter(Q(quotation=models.F('paid')))
        elif value.lower() == 'false':
            return queryset.filter(~Q(quotation=models.F('paid')))
        return queryset
