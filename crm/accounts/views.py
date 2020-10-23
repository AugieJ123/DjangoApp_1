from django.shortcuts import render
from django.http import HttpResponse
# Import all the models for querying...
from .models import *

# Create your views here.
def home(request):
    # Querying all the orders and customers in the dashboard
    orders = Order.objects.all()
    customers = Customer.objects.all()

    # Counting all the orders and customers
    total_customers = customers.count()
    total_orders = orders.count()

    # Orders that are delivered
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

    context = {
        'orders': orders, 
        'customers': customers, 
        'total_customers': total_customers, 
        'total_orders': total_orders, 
        'delivered': delivered, 
        'pending': pending
        }
    return render(request, 'accounts/dashboard.html', context)

def products(request):
    # Query all the products in the database...
    products = Product.objects.all()
    return render(request, 'accounts/products.html', {'products': products})

def customer(request):
    return render(request, 'accounts/customer.html')