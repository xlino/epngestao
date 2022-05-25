# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators  import  login_required
from .filters import OrderFilter
from .models import *
from .forms import OrderForm, CreateUserForm, CustomerForm
from .filters import OrderFilter
from .decorators import unauthenticated_user, allowed_users, admin_only
#import locale

# Create your views here.
#def teste(request):
#    return render(request, 'projetos/teste.html')



#@unauthenticated_user
def registerPage(request):
        form = CreateUserForm()
        if request.method == 'POST':
                form = CreateUserForm(request.POST)
                if form.is_valid():
                        user = form.save()
                        username = form.cleaned_data.get('username')

                        messages.success(request, 'Account was created for ' + username)

                        return redirect('projetos/login')

        context = {'form': form}
        return render(request, 'projetos/register.html', context)


#@unauthenticated_user
def loginPage(request):
        if request.method == 'POST':
                username = request.POST.get('username')
                password = request.POST.get('password')

                user = authenticate(request, username=username, password=password)

                if user is not None:
                        login(request, user)
                        return redirect('home')
                else:
                        messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'projetos/login.html', context)


def logoutUser(request):
        logout(request)
        return redirect('login')



@login_required
#@admin_only
def dashboard(request):
        orders = Order.objects.all()
        customers = Customer.objects.all()

        total_customers = customers.count()

        total_orders = orders.count()
        delivered = orders.filter(status='Delivered').count()
        pending = orders.filter(status='Pending').count()

        context = {'orders': orders, 'customers': customers,
                   'total_orders': total_orders, 'delivered': delivered,
                   'pending': pending}

        return render(request, 'projetos/dashboard.html', context)


#@login_required(login_url='login')
#@allowed_users(allowed_roles=['customer'])
def userPage(request):
        orders = request.user.customer.order_set.all()

        total_orders = orders.count()
        delivered = orders.filter(status='delivered').count()
        pending = orders.filter(status='pending').count()
        print("ORDERS1", orders)

        context = {'orders': orders, 'total_orders': total_orders, 'delivered': delivered,
                   'pending': pending}
        return render(request, 'projetos/user.html', context)


#@login_required(login_url='login')
#@allowed_users(allowed_roles=['customer'])
def accountSettings(request):
        customer = request.user.customer
        form = CustomerForm(instance=customer)

        if request.method == 'POST':
                form = CustomerForm(request.POST, request.FILES, instance=customer)
                if form.is_valid():
                        form.save()
        context = {'form': form}

        return render(request, 'projetos/account_settings.html', context)



#@login_required(login_url='login')
#@allowed_users(allowed_roles=['admin', 'customer'])
def products(request):
        products = Product.objects.all()

        return render(request, 'projetos/products.html', {'products': products})

def status(request):

        orders = Order.objects.all()
        customers = Customer.objects.all()

        total_customers = customers.count()

        total_orders = orders.count()
        delivered = orders.filter(status='Delivered').count()
        pending = orders.filter(status='Pending').count()

        context = {'orders': orders, 'customers': customers,
                   'total_orders': total_orders, 'delivered': delivered,
                   'pending': pending}

        return render(request, 'projetos/status.html', context)



#@login_required(login_url='login')
#@allowed_users(allowed_roles=['admin'])
def customer(request):
        customer = Customer.objects.all()

        return render(request, 'projetos/customer.html')

def testex(request):
    return render(request, 'projetos/testex.html')

def criacustomer(request):
        customer = Customer.objects.all()

        return render(request, 'projetos/criacustomer.html', {'customer': customer})

#@login_required(login_url='login')
#@allowed_users(allowed_roles=['admin'])
def createOrder(request):
        OrderFormSet = inlineformset_factory(Customer, Order, fields=('product', 'status'), extra=10)
        customer = Customer.objects.get(id=pk)
        formset = OrderFormSet(queryset=Order.objects.none(), instance=customer)
        # form = OrderForm(initial={'customer':customer})
        if request.method == 'POST':
                # print('Printing POST:', request.POST)
                form = OrderForm(request.POST)
                formset = OrderFormSet(request.POST, instance=customer)
                if formset.is_valid():
                        formset.save()
                        return redirect('/')

        context = {'form': formset}
        return render(request, 'projetos/order_form.html', context)


#@login_required(login_url='login')
#@allowed_users(allowed_roles=['admin'])
def updateOrder(request, pk):
        order = Order.objects.get(id=pk)
        form = OrderForm(instance=order)
        if request.method == 'POST':
                form = OrderForm(request.POST, instance=order)
                if form.is_valid():
                        form.save()
                        return redirect('/')
        context = {'form': form}
        return render(request, 'projetos/order_form.html', context)

# Create ORDERS  views here.
def orderlist(request):
    return render(request, 'projetos/orderlist.html')

#@login_required(login_url='login')
#@allowed_users(allowed_roles=['admin'])
def deleteorder(request, id):
        order = get_object_or_404(Order, pk=id)
        form = OrderForm(request.POST or None, request.FILES or None, instance=order)
        if request.method == "POST":
                order.delete()
                return redirect('dashboard')
        return render(request, 'projetos/order_delete_confirm.html', {'order': order})

def updateorder(request, id):
        order = get_object_or_404(Order, pk=id)
        form = OrderForm(request.POST or None, request.FILES or None, instance=order)
        if form.is_valid():
                form.save()
                return redirect('dashboard')
        return render(request, 'projetos/order_form.html', {'form': form})


# Create CUSTOMERS views here.
def customerlist(request):
    return render(request, 'projetos/customerlist.html')

def deletecustomer(request, id):
        customer = get_object_or_404(Customer, pk=id)
        form = CustomerForm(request.POST or None, request.FILES or None, instance=customer)
        if request.method == "POST":
                customer.delete()
                return redirect('dashboard')
        return render(request, 'projetos/customer_delete_confirm.html', {'customer': customer})

def updatecustomer(request, id):
        customer = get_object_or_404(Customer, pk=id)
        form = CustomerForm(request.POST or None, request.FILES or None, instance=customer)
        if form.is_valid():
                form.save()
                return redirect('dashboard')
        return render(request, 'projetos/customer_form.html', {'form': form})

def customer_new(request):
    form = CustomerForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('dashboard')
    return render(request, 'projetos/customer_form.html', {'form': form})