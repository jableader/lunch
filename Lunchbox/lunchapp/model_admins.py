__author__ = 'Jableader'
from models import *
from django.contrib import admin

class ItemAdmin(admin.ModelAdmin):
    fields = ['canteen', 'name', 'description', 'price', 'image']

class ItemInline(admin.StackedInline):
    model = Item

class GroupInline(admin.StackedInline):
    model = Group

class MenuAdmin(admin.ModelAdmin):
    fields = ['name', 'canteen']

class GroupAdmin(admin.ModelAdmin):
    fields = ['name', 'menu', 'items']
