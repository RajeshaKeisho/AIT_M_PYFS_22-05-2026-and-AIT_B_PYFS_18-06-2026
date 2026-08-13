from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='books'),
    path('dashboard', views.sales_dashboard, name='dashbaord'),
    path('rawsql', views.raw_sql_view, name='rawsql'),

    path('customers/', views.customer_orders, name='customer_orders'),
    path('search/', views.book_search, name='book_search'),
]
