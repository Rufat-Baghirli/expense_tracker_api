import django
django.setup()

import datetime
import uuid
import pytest
from django.contrib.auth import get_user_model
from budgets.models import BudgetGoal
from datetime import date

User = get_user_model()

@pytest.mark.django_db
def test_budget_goal_creation():
    email = f'test_{uuid.uuid4().hex[:8]}@example.com'
    user = User.objects.create_user(email=email, password='testpass123')
    budget = BudgetGoal.objects.create(
        user=user,
        month=date(datetime.datetime.now().year, datetime.datetime.now().month, 1),
        max_expense=500
    )
    assert budget.user == user
    assert budget.max_expense == 500
