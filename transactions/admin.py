from django.contrib import admin
from .models import Transaction

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('user', 'category', 'amount', 'date', 'description', 'created_at')
    list_filter = ('category', 'date')
    search_fields = ('user__email', 'description')
