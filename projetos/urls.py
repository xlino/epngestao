from django.urls import path
from django.contrib.auth import views as auth_views
from .views import orderlist

from . import views

urlpatterns = [
        path('testex/', views.testex, name="testex"),

        path('register/', views.registerPage, name="register"),
        #path('login/', views.loginPage, name="login"),
        #path('logout/', views.logoutUser, name="logout"),

        path('dashboard/', views.dashboard, name="dashboard"),

        path('user/', views.userPage, name="user-page"),

        path('account/', views.accountSettings, name="account"),

        path('products/', views.products, name="products"),
        path('status/', views.status, name="status"),

        path('customer/', views.customer, name="customer"),
        path('criacustomer/', views.criacustomer, name="criacustomer"),
        #path('order_form/', views.createOrder, name="order_form"),
        #path('update_order/<str:pk>/', views.updateOrder, name="update_order"),
        #path('delete_order/<str:pk>/', views.deleteOrder, name="delete_order"),

        path('orderlist/', views.orderlist, name="orderlist"),
        path('updateorder/', views.updateorder, name="updateorder"),
        path('deleteorder/', views.deleteorder, name="deleteorder"),

        path('updatecustomer/', views.updatecustomer, name="updatecustomer"),
        path('deletecustomer/', views.deletecustomer, name="deletecustomer"),

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


