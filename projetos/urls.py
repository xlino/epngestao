from django.urls import path
from django.contrib.auth import views as auth_views
from .views import orderlist

from . import views
from .views import deleteorder
from .views import updateorder

from .views import customer_new
from .views import deletecustomer
from .views import updatecustomer

urlpatterns = [
        path('register/', views.registerPage, name="register"),
        path('user/', views.userPage, name="user-page"),
        path('account/', views.accountSettings, name="account"),

#URL_CURRICULO
        path('testex/', views.testex, name="testex"),

#URL_DASHBOARD
        path('dashboard/', views.dashboard, name="dashboard"),


        path('products/', views.products, name="products"),
        path('status/', views.status, name="status"),
        path('customer/', views.customer, name="customer"),
        path('criacustomer/', views.criacustomer, name="criacustomer"),

#URLs ORDER
        path('deleteorder/<int:id>/', deleteorder, name="deleteorder"),
        path('orderlist/', views.orderlist, name="orderlist"),
        path('updateorder/<int:id>/', updateorder, name="updateorder"),

#URLs CUSTOMER
        path('deletecustomer/<int:id>/', deletecustomer, name="deletecustomer"),
        path('customerlist/', views.customerlist, name="customerlist"),
        path('updatecustomer/<int:id>/', updatecustomer, name="updatecustomer"),
        path('customer_new/', customer_new, name="customer_new"),

#URLs PASSWORD
        path('reset_password/', auth_views.PasswordResetView.as_view(
                template_name="accounts/password_reset.html"), name="reset_password"),
        path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(
                template_name="accounts/password_reset_sent.html"), name="password_reset_done"),
        path('reset/<uid64>/<token>', auth_views.PasswordResetConfirmView.as_view(
                template_name="accounts/password_reset_form.html"
        ), name="password_reset_confirm"),
        path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(
                template_name="accounts/password_reset_done.html"
        ), name="password_reset_complete"),

]


