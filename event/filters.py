from django_filters import rest_framework as filters

from event.models import Event


class EventFilter(filters.FilterSet):
    """
    filter the event by client's first name or last name.
    filter the attendees less than a certain number
    filter the event that has not assigned a technique support
    """
    attendees_less_than = filters.NumberFilter(field_name='attendees', lookup_expr='lte')
    assigned_to_eq_null = filters.BooleanFilter(field_name='assigned_to', lookup_expr='isnull', label='no support was '
                                                                                                      'assigned')

    class Meta:
        model = Event
        fields = {'client__first_name': ['icontains'],
                  'client__last_name': ['icontains'],
                  }
