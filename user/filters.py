from django_filters import rest_framework as filters

from user.models import User


class UserFilter(filters.FilterSet):
    """
    filter the users by their department
    filter the users by their first name or last name or phone number or username
    ordering the users list by user's first name, last name, phone number, username
    """
    filter_by_department = filters.ChoiceFilter(field_name='department',
                                                choices=[(choice.name, choice.value) for choice in
                                                         User.DepartmentChoice],
                                                label='filter by department')
    ordering = filters.OrderingFilter(
        fields=(('first_name', 'ordering by first name'), ('last_name', 'ordering by last name'),
                ('phone', 'ordering by phone number'), ('username', 'ordering by username'))
    )

    class Meta:
        model = User
        fields = {
            'first_name': ['icontains'],
            'last_name': ['icontains'],
            'username': ['exact'],
        }
