from django.db import models
from django.conf import settings

class BudgetGoal(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="budget_goals")
    month = models.DateField(help_text="Budget for this month (use first day of the month)")
    max_expense = models.DecimalField(max_digits=12, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'month')
        ordering = ['-month']

    def __str__(self):
        return f"{self.user.email} - {self.month.strftime('%Y-%m')} - {self.max_expense}"
