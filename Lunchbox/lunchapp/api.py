__author__ = 'Jableader'
from django.http import  HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
import json
from models import *
import braintree

def canteen(request, user_pk):
    return HttpResponse(json.dumps(User.objects.get(pk=user_pk).parent.canteen.dict()), 'text/json')

def kids(request, user_pk):
    kids = User.objects.get(pk=user_pk).parent.kid_set.all()
    return HttpResponse(json.dumps([k.dict() for k in kids]), 'text/json')

def auth(request):
    user = authenticate(username='Roger', password='password')
    if user is None: return HttpResponse('{pk:-1}', 'text/json')
    else: return HttpResponse(json.dumps({'pk': user.pk}), 'text/json')

@csrf_exempt
def getToken(request, client_id):
    token = braintree.ClientToken.generate({
        'customer_id':client_id
    })

    return HttpResponse(token)


def makepayment(card, cost):
    braintree.Configuration.configure(
        braintree.Environment.Sandbox,
        'rnk5xkqh7zsfmq8r',
        '37fxzhxy939jn9rz',
        'e54c4c1d837027f2b0dc6f50fccc8fcc'
    )

    return braintree.Transaction.sale({
        "amount": "%.2f" % cost,
        "credit_card": card
    })


@csrf_exempt
def makeOrder(request):
    order = json.loads(request.POST['order'])
    kid = Kid.objects.get(pk=order['kidId'])
    items = [Item.objects.get(pk=pk) for pk in order['itemIds']]
    order = Order.objects.create(kid = kid, comment = order['comment'])

    order.save()

    map(order.items.add, items)

    cost = sum([i.price for i in order.items.all()])
    card = json.loads(request.POST['card'])

    if makepayment(card, cost).is_success:
        return HttpResponse('{success: true}')
    else:
        order.delete()
        return HttpResponse('{success: false}')