from rest_framework import viewsets, permissions
from .models import BudgetGoal
from .serializers import BudgetGoalSerializer

class BudgetGoalViewSet(viewsets.ModelViewSet):
    serializer_class = BudgetGoalSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return BudgetGoal.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
