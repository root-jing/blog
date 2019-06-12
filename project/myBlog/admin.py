from django.contrib import admin
from .models import Sender
#user:yjs
#password:123456789a
# Register your models here.

class SenderAdmin(admin.ModelAdmin):

    list_display = ['pk','name','ps','age','gender','title','contents','lasttime','isDelete']
    list_filter = ['gender']
    search_fields = ['title','name']
    list_per_page = 5
    fieldsets = [('number',{'fields':['age']}),
                 ('base',{'fields':['name','ps','isDelete',]})]
admin.site.register(Sender,SenderAdmin)

