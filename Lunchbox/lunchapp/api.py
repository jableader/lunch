__author__ = 'Jableader'
from django.http import  HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

import json
from models import *

def canteen(request, user_pk):
    return HttpResponse(json.dumps(User.objects.get(pk=user_pk).parent.canteen.dict()), 'text/json')

def kids(request, user_pk):
    kids = User.objects.get(pk=user_pk).parent.kid_set.all()
    return HttpResponse(json.dumps([k.dict() for k in kids]), 'text/json')

def auth(request):
    user = authenticate(username='Roger', password='password')
    if user is None: return HttpResponse('{pk:-1}', 'text/json')
    else: return HttpResponse(json.dumps({'pk': user.pk}), 'text/json')

def makeOrder(request):
    return #make some order