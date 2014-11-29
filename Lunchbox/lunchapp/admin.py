from django.contrib import admin
from model_admins import ItemAdmin, GroupAdmin, MenuAdmin

import models

# Register your models here.
admin.site.register(models.Canteen)
admin.site.register(models.LunchLady)
admin.site.register(models.Parent)
admin.site.register(models.Kid)
admin.site.register(models.Menu, MenuAdmin)
admin.site.register(models.Group, GroupAdmin)
admin.site.register(models.Item, ItemAdmin)
admin.site.register(models.Special)