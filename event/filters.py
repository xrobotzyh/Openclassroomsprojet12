from django_filters import rest_framework as filters

from event.models import Event



class EventFilter(filters.FilterSet):
    attendees_less_than = filters.NumberFilter(field_name='attendees', lookup_expr='lte')
    assigned_to_eq_null = filters.BooleanFilter(field_name='assigned_to', lookup_expr='isnull',label='no support was '
                                                                                                     'assigned')

    class Meta:
        model = Event
        fields = {'client__first_name': ['icontains'],
                  'client__last_name': ['icontains'],
                  }
