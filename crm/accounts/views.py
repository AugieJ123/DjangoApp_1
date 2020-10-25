from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
# Import all the models for querying...
from .models import *
# Importing the form class to create form
from .form import OrderForm

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

def customer(request, pk):
    # Query customer by id
    customer = Customer.objects.get(id=pk)

    # Query the order made by the customer
    orders = customer.order_set.all()

    # Counting the orders made by the customer
    order_count = orders.count()

    context = {'customer': customer, 'orders': orders, 'order_count': order_count}
    return render(request, 'accounts/customer.html', context)

def createOrder(request):
    form = OrderForm()
    if request.method == 'POST':
        #print('Printing POST:', request.POST )
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'accounts/order_form.html', context)

def updateOrder(request, pk):
    # Query the order to update
    order = Order.objects.get(id=pk)

    form = OrderForm(instance=order)
    if request.method == 'POST':
        #print('Printing POST:', request.POST )
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form,}
    return render(request, 'accounts/order_form.html', context)

def deleteOrder(request,pk=id):
    order = get_object_or_404(Order, pk=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('/')

    context = {'item': order}
    return render(request, 'accounts/delete.html', context)