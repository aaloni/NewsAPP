from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from . import models

#Requested fields in Admin account
class CustomUserAdmin(UserAdmin):
    list_display = (
        'first_name', 'last_name', 'username', 'email',
        'phone','national_id','is_staff','birth_date'
    )


#Articles fields in Admin account
admin.site.register(models.Article)
admin.site.register(CustomUser, CustomUserAdmin)


