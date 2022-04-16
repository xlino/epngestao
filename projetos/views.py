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



#@login_required(login_url='login')
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

def testex(request):
    return render(request, 'projetos/testex.html')

#@login_required(login_url='login')
#@allowed_users(allowed_roles=['admin', 'customer'])
def products(request):
        products = Product.objects.all()

        return render(request, 'projetos/products.html', {'products': products})


#@login_required(login_url='login')
#@allowed_users(allowed_roles=['admin'])
def customer(request):
        customer = Customer.objects.get(id=pk_test)

        orders = customer.order_set.all()
        order_count = orders.count()

        myFilter = OrderFilter(request.GET, queryset=orders)
        orders = myFilter.qs

        context = {'customer': customer, 'orders': orders, 'order_count': order_count,
                   'myFilter': myFilter}
        return render(request, 'projetos/customer.html', context)


#@login_required(login_url='login')
#@allowed_users(allowed_roles=['admin'])
def createorder(request):
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


#@login_required(login_url='login')
#@allowed_users(allowed_roles=['admin'])
def deleteOrder(request, pk):
        order = Order.objects.get(id=pk)
        if request.method == "POST":
                order.delete()
                return redirect('/')

        context = {'item': order}
        return render(request, 'projetos/delete.html', context)