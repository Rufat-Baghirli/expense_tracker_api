from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework.throttling import UserRateThrottle

from core.audit import log_user_action
from .models import Transaction, Category
from .serializers import TransactionSerializer, CategorySerializer
from .services import TransactionService
from .filters import TransactionFilter
from django_filters.rest_framework import DjangoFilterBackend

class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]
    throttle_classes = [UserRateThrottle]

    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TransactionViewSet(viewsets.ModelViewSet):
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticated]
    throttle_classes = [UserRateThrottle]
    filter_backends = [DjangoFilterBackend]
    filterset_class = TransactionFilter

    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        instance = serializer.save(user=self.request.user)
        log_user_action(self.request.user, "Created Transaction", str(instance.id))

    @action(detail=False, methods=['get'])
    def summary(self, request):
        """
        Returns total income, total expense, and balance for a given month/year.
        Example: /api/transactions/summary/?month=07&year=2025
        """
        year = int(request.query_params.get('year'))
        month = int(request.query_params.get('month'))

        service = TransactionService(request.user)
        data = service.monthly_summary(year=year, month=month)
        return Response(data)

    @action(detail=False, methods=['get'])
    def export(self, request):
        """
        Returns all user's transactions as downloadable CSV.
        Example: /api/transactions/export/
        """
        service = TransactionService(request.user)
        csv_data = service.export_to_csv()

        response = HttpResponse(csv_data, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=transactions.csv'
        return response
