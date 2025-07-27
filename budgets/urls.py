from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BudgetGoalViewSet

router = DefaultRouter()
router.register('budget-goals', BudgetGoalViewSet, basename='budgetgoal')

urlpatterns = [
    path('', include(router.urls)),
]
