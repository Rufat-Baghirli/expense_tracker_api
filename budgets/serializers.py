from rest_framework import serializers
from .models import BudgetGoal

class BudgetGoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = BudgetGoal
        fields = ['id', 'month', 'max_expense', 'created_at']
        read_only_fields = ['created_at']
