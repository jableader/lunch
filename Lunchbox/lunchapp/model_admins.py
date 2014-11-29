__author__ = 'Jableader'
from models import *
from django.contrib import admin

class ItemAdmin(admin.ModelAdmin):
    fields = ['name', 'description', 'price', 'image']

class ItemInline(admin.StackedInline):
    model = Item

class GroupInline(admin.StackedInline):
    model = Group

class MenuAdmin(admin.ModelAdmin):
    fields = ['name']

class GroupAdmin(admin.ModelAdmin):
    fields = ['name', 'menu', 'items']
