from user.models import User


def is_sales(user_id):
    return User.objects.get(id=user_id).department == 'sales'


def is_support(user_id):
    return User.objects.get(id=user_id).department == 'support'


def is_management(user_id):
    return User.objects.get(id=user_id).department == 'management'
