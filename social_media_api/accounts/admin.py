from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
   fieldsets = UserAdmin.fieldsets + (
        ('Profile', {'fields': ('bio', 'profile_picture', 'followers')}),
   )
   add_fieldsets = UserAdmin.add_fieldsets + (
   (None, {'fields': ('bio', 'profile_picture')}),
   )
   list_display = ('username', 'email', 'is_active', 'is_staff')
   search_fields = ('username', 'email')
