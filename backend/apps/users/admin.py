from secrets import token_bytes
from django.contrib import admin

from apps.users.models import User

# Register your models here.


@admin.register(User)
class UserModel(admin.ModelAdmin):
    fields = ['name', 'email', 'token', 'token_expires_at']

    list_filter = []
    list_display = fields
    search_fields = ['name', 'email']
