from django.contrib import admin
from .models import Account

# Register your models here.
@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('site', 'login', 'owner', 'created_at', 'password_changed_at')  # исправлено
    search_fields = ('site', 'login')
    list_filter = ('owner',)  