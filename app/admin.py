from django.contrib.gis import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.admin import GroupAdmin

# Import models
from .models import CustomUser
from .models import CustomGroup
from .models import Location


# Register models for admin
admin.site.register(CustomUser, UserAdmin)
admin.site.register(CustomGroup, GroupAdmin)
admin.site.register(Location, admin.OSMGeoAdmin)
