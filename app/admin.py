from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.admin import GroupAdmin

# Import models
from .models import CustomUser
from .models import CustomGroup


# Register models for admin
admin.site.register(CustomUser, UserAdmin)
admin.site.register(CustomGroup, GroupAdmin)
