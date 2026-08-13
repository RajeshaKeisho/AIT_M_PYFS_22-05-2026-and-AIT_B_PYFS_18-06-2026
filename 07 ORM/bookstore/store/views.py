from django.shortcuts import render
from .models import *
from django.db.models import Sum, F, Count, Q
from django.db import connection


# Create your views here.

def book_list(request):
    books = Book.objects.select_related('author')
    return render(request, 'books.html', {'books':books})

def sales_dashboard(request):
    books = Book.objects.annotate(total_sold = Sum('orderitem__quantity'))
    return render(request, 'dashboard.html', {'books':books})


def raw_sql_view(request):
    
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT title, price FROM store_book
""")
        rows = cursor.fetchall()
        return render(request, 'raw.html', {'rows':rows})


# View 4: Customer Order Summary
def customer_orders(request):
    customers = Customer.objects.annotate(
        total_orders=Count('order'),
        total_items=Sum('order__orderitem__quantity')
    ).order_by('-total_orders')

    return render(
        request,
        'customer_orders.html',
        {'customers': customers}
    )


# View 5: Book Search and Filtering
def book_search(request):
    query = request.GET.get('q', '')

    books = Book.objects.select_related('author').filter(
        Q(title__icontains=query) |
        Q(author__name__icontains=query)
    ).order_by('title')

    return render(
        request,
        'book_search.html',
        {
            'books': books,
            'query': query
        }
    )