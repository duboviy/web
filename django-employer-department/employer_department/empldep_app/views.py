from django.core import serializers
from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404

from .models import Employee


def users_json(request):
    users = Employee.objects.all()
    data = serializers.serialize("json", users,
                                 fields=('first_name', 'last_name', 'department'),
                                 use_natural_keys=True)
    return HttpResponse(data, content_type='application/json')


def user_json(request, user_id):
    try:
        user_id = int(user_id)
    except ValueError:
        raise Http404()
    user = get_object_or_404(Employee, pk=user_id)
    data = serializers.serialize("json", [user],
                                 fields=('first_name', 'last_name', 'department'),
                                 use_natural_keys=True)
    return HttpResponse(data, content_type='application/json')
