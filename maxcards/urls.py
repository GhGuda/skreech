from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("auth/login", views.login, name="login"),
    path("logout", views.logout, name="logout"),
    path("u/register", views.register, name="register"),


    path("credit_card", views.credit_card, name="credit_card"),
    path("proceed_order/<card>", views.payment, name="payment"),
    path("bitcion_pay/<card>", views.bitcoin, name="bitcoin"),
    path("momo_pay/<card>", views.mobilemoney, name="mobilemoney"),
    path("bank_pay/<card>", views.banktransfer, name="banktransfer"),
    path("del_order/this/yu8304309fwqebq9803u9qhi/<card>/8948yrw8963fjsyiofuiwerunfiasfierwifuoayfu", views.del_order, name="del_order"),
    path("my_orders", views.orders, name="orders"),


]
