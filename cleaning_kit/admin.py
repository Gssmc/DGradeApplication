from django.contrib import admin

from .models import (KitCategory,CleaningKit,
            Order,Notification)




admin.site.register(KitCategory)
admin.site.register(CleaningKit)
admin.site.register(Order)
admin.site.register(Notification)
