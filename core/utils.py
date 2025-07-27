import csv
from django.http import HttpResponse

def export_transactions_to_csv(queryset):
    """
    Export the given queryset of transactions to a CSV file
    and return an HttpResponse object for download.
    """
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="transactions.csv"'

    writer = csv.writer(response)
    writer.writerow(['Date', 'Type', 'Category', 'Amount', 'Description'])

    for t in queryset:
        writer.writerow([
            t.date,
            t.type,
            t.category.name if t.category else '',
            t.amount,
            t.description
        ])

    return response
