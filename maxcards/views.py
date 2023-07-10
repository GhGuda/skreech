from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth import login, logout
from .models import *
from django.contrib.auth.decorators import login_required
# from django.core.mail import send_mail
# from django.conf import settings
# from django.contrib.auth import get_user_model
# from django_email_verification import sendConfirm


# Create your views here.


def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username taken, try new one!")
                return redirect('register')
            
            elif len(password) < 8:
                messages.info(request, "Password is weak, try new one!")
                return redirect('register')
            
            elif len(username) == 0:
                messages.info(request, "Enter your username!")
                return redirect('register')
            
            elif len(email) == 0:
                messages.info(request, "Enter your email!")
                return redirect('register')
            
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email taken, try new one!")
                return redirect('register')
            
            else:
                new_user = User.objects.create_user(username=username, email=email, password=password)
                new_user.save()
                return redirect("login")
        else:
            messages.info(request, "Password did'nt match, try again!")
            return redirect('register')
    else:        
        return render(request, "index.html")
    

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        auth_user = auth.authenticate(username=username, password=password)
        
        if auth_user is not None:
            auth.login(request, auth_user)
            return redirect('index')
        else:
            messages.info(request, "No user found for this username/password.")
            return redirect('login')

    else:
        return render(request, "login.html")
    

def logout(request):
    auth.logout(request)
    return redirect('index')

def index(request):
    return render(request, "frontpage.html")


def credit_card(request):
    card = Cards.objects.all()


    context={
        "cards":card,
    }
    return render(request, "pricing.html", context)


@login_required(login_url="login")
def payment(request, card):
    order = Cards.objects.get(card_id=card)

    return render(request, "payment.html", {"card":order})
    

@login_required(login_url="login")
def bitcoin(request, card):
    order = Cards.objects.get(card_id=card)
    if request.method == "POST":
        user = request.user.username
        image = request.FILES.get('post_img')
        transaction = "Bitcoin(BTC)"
        if image != None:
            new_payment = Payment_screenshot.objects.create(user=user, transaction_type=transaction, image=image)
            new_payment.save()


            new_order = User_orders(user=request.user, card=order, transaction_type=transaction)
            new_order.save()
            return redirect('orders')
        else:
            messages.info(request, "Upload payments screenshot to proceed.")
            return redirect('bitcoin', card)

    return render(request, "bitcoin.html", {"card":order})


@login_required(login_url="login")
def mobilemoney(request, card):
    order = Cards.objects.get(card_id=card)
    if request.method == "POST":
        user = request.user.username
        image = request.FILES.get('post_img')
        transaction = "MoMo"

        
        if image != None:
            new_payment = Payment_screenshot.objects.create(user=user, transaction_type=transaction, image=image)
            new_payment.save()


            new_order = User_orders(user=request.user, card=order, transaction_type=transaction)
            new_order.save()
            return redirect('orders')
        else:
            messages.info(request, "Upload payments screenshot to proceed.")
            return redirect('mobilemoney', card)

    return render(request, "mobilemoney.html", {"card":order})



@login_required(login_url="login")
def banktransfer(request, card):
    order = Cards.objects.get(card_id=card)

    if request.method == "POST":
        user = request.user.username
        image = request.FILES.get('post_img')
        transaction = "Bank"
        if image != None:
            new_payment = Payment_screenshot.objects.create(user=user, transaction_type=transaction, image=image)
            new_payment.save()

            new_order = User_orders(user=request.user, card=order, transaction_type=transaction)
            new_order.save()
            return redirect('orders')
        else:
            messages.info(request, "Upload payments screenshot to proceed.")
            return redirect('banktransfer', card)
    return render(request, "banktransfer.html", {"card":order})



@login_required(login_url="login")
def orders(request):
    order = User_orders.objects.filter(user=request.user)

    return render(request, "orders.html", {"order":order})


def del_order(request, card):
    order = User_orders.objects.get(id=card)
    order.delete()
    return redirect("orders")



# def sendEamil(request):
#     password = request.POST.get('password')
#     username = request.POST.get('username')
#     email = request.POST.get('email')

#     user = get_user_model().objects.create(username=username, password=password, email=email)
#     sendConfirm(user)
#     return render(request, 'confirm_email.html')