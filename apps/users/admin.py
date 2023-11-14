from django.contrib.auth.admin import UserAdmin
from django.contrib import admin

from .models import BaseUser


admin.site.register(BaseUser, UserAdmin)
