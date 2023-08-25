from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

#from django import http
#from django.contrib import messages
#from mptt.admin import DraggableMPTTAdmin, MPTTAdminForm


# Register your models here.
class CustomUserAdmin(UserAdmin):
    list_display = ( 'email', 'username','is_staff', 'date_joined', 'last_login')
    search_fields = ('email', 'username',)
    readonly_fields = ('email', 'username',)
    list_editable = ('is_staff',)

    filter_horizontal = ()
    list_filter = ('is_admin', 'is_staff')
    fieldsets = ()
    
admin.site.register(CustomUser, CustomUserAdmin)
