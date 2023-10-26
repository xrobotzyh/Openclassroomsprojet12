from django.http import HttpResponse


def trigger_error(request):
    division_by_zero = 1 / 0
    return HttpResponse(f'The result is {division_by_zero}')
