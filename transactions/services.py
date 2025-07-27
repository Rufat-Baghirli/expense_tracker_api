from .models import Transaction
from django.db.models import Sum
from collections import defaultdict
import csv
import io

class TransactionService:
    def __init__(self, user):
        self.user = user

    def monthly_summary(self, year, month):
        queryset = Transaction.objects.filter(user=self.user, date__year=year, date__month=month)
        total_income = queryset.filter(type='INCOME').aggregate(total=Sum('amount'))['total'] or 0
        total_expense = queryset.filter(type='EXPENSE').aggregate(total=Sum('amount'))['total'] or 0
        return {
            'income': total_income,
            'expense': total_expense,
            'balance': total_income - total_expense
        }

    def export_to_csv(self):
        output = io.StringIO()
        writer = csv.writer(output)
        writer.writerow(['Date', 'Type', 'Amount', 'Category', 'Description'])

        for txn in Transaction.objects.filter(user=self.user).select_related('category'):
            writer.writerow([
                txn.date,
                txn.type,
                txn.amount,
                txn.category.name if txn.category else '',
                txn.description
            ])

        return output.getvalue()
