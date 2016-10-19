from django.shortcuts import render_to_response

from models import todo


def index(request):
    items = todo.objects.all()
    return render_to_response('index.html', {'items': items}) 
