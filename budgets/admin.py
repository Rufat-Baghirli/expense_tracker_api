from django.contrib import admin
from .models import BudgetGoal

@admin.register(BudgetGoal)
class BudgetGoalAdmin(admin.ModelAdmin):
    list_display = ('user', 'month', 'max_expense', 'created_at')
    list_filter = ('month',)
    search_fields = ('user__email',)
