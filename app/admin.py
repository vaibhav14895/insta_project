from django.contrib import admin
from .models import ProfileUser,Status
# Register your models here.
class service(admin.ModelAdmin):
    list_display=('uid','name','photo')
    
admin.site.register(ProfileUser,service)

class status(admin.ModelAdmin):
    list_display=('user','file')
    
admin.site.register(Status)
    