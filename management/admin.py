from django.contrib import admin
from .models import (GarbageCategory,Garbage
    ,Cleaner,GarbageOrder)


#this is to customize garbage admin model display
class GarbageAdmin(admin.ModelAdmin):

    list_display = ['__str__', 'slug','status','weight',]

    class Meta:
        model=Garbage

class CleanerAdmin(admin.ModelAdmin):

    list_display = ['__str__', 'name','cleaning_task','price','contact']

    class Meta:
        model=Cleaner


admin.site.register(Cleaner,CleanerAdmin)
admin.site.register(Garbage,GarbageAdmin)
admin.site.register(GarbageCategory)
admin.site.register(GarbageOrder)