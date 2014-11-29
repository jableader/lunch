from django.db import models
from django.conf import settings

from lunch.settings import STATIC_URL


def imgurl(url): return STATIC_URL + 'img/uploaded' + url[1:]

class Canteen(models.Model):
    name = models.CharField(max_length=120)
    address = models.CharField(max_length=320)

    def dict(self):
        return {
            'name': self.name,
            'address': self.address,
            'menuIds': [m.dict() for m in self.menu_set.all()],
            'pk': self.pk
        }

    def __str__(self): return self.name

class LunchLady(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    canteen = models.ForeignKey(Canteen)

    def __str__(self): return self.user.username

class Parent(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    canteen = models.ForeignKey(Canteen)

    def dict(self):
        return {
            'username': self.user.username,
            'kidIds': [k.dict() for k in self.kid_set.all()],
            'canteenId': self.canteen.dict(),
            'pk': self.user_id
        }

    def __str__(self): return self.user.username

class Kid(models.Model):
    parent = models.ForeignKey(Parent)
    name = models.CharField(max_length=32)
    room = models.CharField(max_length=100)
    image = models.FileField()

    def dict(self):
        return {'name': self.name, 'room': self.room, 'pk': self.pk, 'image': imgurl(self.image.url)}

    def __str__(self): return self.name

class Item(models.Model):
    canteen = models.ForeignKey(Canteen)
    image = models.FileField()
    price = models.FloatField()
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=140)

    def dict(self):
        return {
            'pk': self.pk,
            'image': imgurl(self.image.url),
            'price': self.price,
            'name': self.name,
            'description': self.description
        }

    def __str__(self): return self.name


class Menu(models.Model):
    canteen = models.ForeignKey(Canteen)
    name = models.CharField(max_length=32)

    def dict(self):
        return {
            'name': self.name,
            'groupIds': [g.dict() for g in sorted(self.group_set.all(), lambda x, y: y.priority - x.priority)],
            'specialIds': [s.dict() for s in self.special_set.all()],
            'pk': self.pk,
        }

    def __str__(self):return self.name


class Special(models.Model):
    menu = models.ForeignKey(Menu)
    item = models.OneToOneField(Item)
    specialImage = models.FileField()

    def dict(self): return {'itemId': self.item.dict(), 'specialImage': imgurl(self.specialImage.name), 'pk': self.pk}

    def __str__(self): return self.item.name

class Group(models.Model):
    name = models.CharField(max_length=32)
    menu = models.ForeignKey(Menu)
    items = models.ManyToManyField(Item)
    priority = models.IntegerField(default=0)

    def dict(self):
        return {
            'name': self.name,
            'itemIds': [item.dict() for item in self.items.all()],
            'pk': self.pk
        }

    def __str__(self): return self.name

class Order(models.Model):
    items = models.ManyToManyField(Item)
    kid = models.ForeignKey(Kid)
    comment = models.CharField(max_length=140)

    def __str__(self): return self.kid.name