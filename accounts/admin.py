from typing import Any
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserChangesForm, UserCreationsForm
from django.contrib.auth.models import Group
from accounts.models import User,OtpCode

@admin.register(OtpCode)
class OtpCodeAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'code', 'created')

class UserAdmin(BaseUserAdmin):
    form = UserChangesForm
    add_form = UserCreationsForm
    
    list_display = ('email', 'phone_number','is_admin')
    list_filter = ('full_name',)
    fieldsets = (
        ('Main',{'fields':('email', 'full_name', 'phone_number', 'password')}),
        ('permission',{'fields':('is_superuser','is_admin','is_active','last_login','groups','user_permissions')}),
    )
    add_fieldsets = (
        (None,{'fields':('email', 'full_name', 'phone_number', 'password1', 'password2')}),
    ) 
    
    readonly_fields = ('last_login',)
    
    search_fields = ('email','full_name')
    ordering = ('full_name',)
    filter_horizontal = ('groups','user_permissions')
    
    def get_form(self, request, obj,**kwargs):
        form = super().get_form(request, obj, **kwargs)
        is_superuser = request.user.is_superuser
        if not is_superuser:
            form.base_fields['is_superuser'].disabled = True
        return form
    

admin.site.register(User,UserAdmin)
    
