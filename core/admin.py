# core/admin.py
from django.contrib import admin
from .models import Item

# Register Item so you can view/manage it at /admin/
@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display  = ('item_name', 'item_type', 'user', 'location', 'reported_at')
    list_filter   = ('item_type',)
    search_fields = ('item_name', 'description', 'location')