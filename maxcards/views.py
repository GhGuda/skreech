from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth import login, logout
from .models import *
from django.contrib.auth.decorators import login_required
import datetime, re
from django.core.mail import send_mail

# Create your views here.


def register(request):
    if request.method == "POST":
        username = request.POST['username'].lower()
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if not re.match(r'^[a-zA-Z0-9_]+$', username):
                messages.error(request, "Username can only contain letters, numbers, and underscores!")
                return redirect('register')
            
            elif username.isdigit(): 
                messages.error(request, "Username cannot consist of only numbers!")
                return redirect('register')
            
            elif len(username) <= 0:
                messages.error(request, "Enter username!")
                return redirect('register')
            
            elif ' ' in username:
                messages.error(request, "Username cannot contain spaces, can only contain letters, numbers, and underscores!")
                return redirect('register')
            
            elif User.objects.filter(username__iexact=username).exists():
                messages.error(request, "Username taken!")
                return redirect('register')
            
            elif password == username:
                messages.error(request, "Password similar to username!")
                return redirect('register')
            
            elif len(email) <= 0:
                messages.error(request, "Enter email!")
                return redirect('register')
            
            elif len(password) < 8:
                messages.error(request, "Password is weak, enter strong password!")
                return redirect('register')
            
            elif User.objects.filter(email=email).exists():
                messages.error(request, "Email taken!")
                return redirect('register')
            else:
                new_user = User.objects.create_user(username=username, email=email, password=password)
                subject = 'Welcome to Maxcards - Your Credit Card Shopping Destination'
                message = f'Hello {username.capitalize()},\n\nWelcome to Maxcards! We are thrilled to have you as a part of our community. At Maxcards, we provide a seamless and secure platform for exploring and acquiring credit cards that suit your needs.\n\nWhether you are looking for rewards, low interest rates, or exclusive benefits, our curated selection has you covered. Our team is dedicated to helping you make informed decisions about your financial future.\n\nThank you for choosing Maxcards. Feel free to explore our offerings and begin your credit card journey today!\n\nBest regards,\nThe Maxcards Team'
                from_email = 'no-reply-maxcards@gmail.com'
                recipient_list = [email]
                send_mail(subject, message, from_email, recipient_list, fail_silently=False)
                new_user.save()
                messages.success(request, 'You have successfully registered!')
                return redirect("/")
        else:
            messages.info(request, "Password did'nt match, try again!")
            return redirect('register')
    else:
        return render(request, "index.html")


def login(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == "POST":
            username = request.POST['username'].lower()
            password = request.POST['password']

            auth_user = auth.authenticate(username=username, password=password)

            if auth_user is not None:
                auth.login(request, auth_user)
                messages.success(request, 'You have successfully registered!')
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
    year = datetime.datetime.now().year

    return render(request, "frontpage.html", { "year":year})


@login_required(login_url="login")
def credit_card(request):
    year = datetime.datetime.now().year
    card = Cards.objects.all()


    context={
        "cards":card,
        "year":year

    }
    return render(request, "pricing.html", context)


@login_required(login_url="login")
def payment(request, card):
    year = datetime.datetime.now().year
    order = Cards.objects.get(card_id=card)

    return render(request, "payment.html", {"card":order, "year":year})


@login_required(login_url="login")
def bitcoin(request, card):
    year = datetime.datetime.now().year
    order = Cards.objects.get(card_id=card)
    if request.method == "POST":
        user = request.user.username
        usermail = request.user.email
        image = request.FILES.get('post_img')
        transaction = "Bitcoin(BTC)"
        if image:
            new_payment = Payment_screenshot.objects.create(user=user, transaction_type=transaction, image=image)
            new_payment.save()


            new_order = User_orders(user=user, card=order, transaction_type=transaction)
            new_order.save()
            
            subject = 'Order Confirmation'
            message = f'Hello {user.capitalize()},\n\nYour order for {order.account_holder} has been confirmed, we will review your payments and get back to you soon.\n\nThank you for choosing our services!\n\nBest regards,\nThe Maxcards Team.'
            from_email = 'no-reply-maxcards@gmail.com'
            recipient_list = [usermail]
            send_mail(subject, message, from_email, recipient_list, fail_silently=False)
            return redirect('orders')
        else:
            messages.info(request, "Upload payments screenshot to proceed.")
            return redirect('bitcoin', card)

    return render(request, "bitcoin.html", {"card":order, "year":year})


@login_required(login_url="login")
def mobilemoney(request, card):
    year = datetime.datetime.now().year
    order = Cards.objects.get(card_id=card)
    if request.method == "POST":
        user = request.user.username
        usermail = request.user.email
        image = request.FILES.get('post_img')
        transaction = "MoMo"


        if image:
            new_payment = Payment_screenshot.objects.create(user=user, transaction_type=transaction, image=image)
            new_payment.save()


            new_order = User_orders(user=user, card=order, transaction_type=transaction)
            new_order.save()
            subject = 'Order Confirmation'
            message = f'Hello {user.capitalize()},\n\nYour order for {order.account_holder} has been confirmed, we will review your payments and get back to you soon.\n\nThank you for choosing our services!\n\nBest regards,\nThe Maxcards Team.'
            from_email = 'no-reply-maxcards@gmail.com'
            recipient_list = [usermail]
            send_mail(subject, message, from_email, recipient_list, fail_silently=False)
            return redirect('orders')
        else:
            messages.error(request, "Upload payments screenshot to proceed.")
            return redirect('mobilemoney', card)

    return render(request, "mobilemoney.html", {"card":order, "year":year})



@login_required(login_url="login")
def banktransfer(request, card):
    year = datetime.datetime.now().year
    order = Cards.objects.get(card_id=card)

    if request.method == "POST":
        user = request.user.username
        usermail = request.user.email
        image = request.FILES.get('post_img')
        transaction = "Bank"

        if image:
            new_payment = Payment_screenshot.objects.create(user=user, transaction_type=transaction, image=image)

            new_order = User_orders(user=user, card=order, transaction_type=transaction)
            new_payment.save()
            new_order.save()
            subject = 'Order Confirmation'
            message = f'Hello {user.capitalize()},\n\nYour order for {order.account_holder} has been confirmed, we will review your payments and get back to you soon.\n\nThank you for choosing our services!\n\nBest regards,\nThe Maxcards Team.'
            from_email = 'no-reply-maxcards@gmail.com'
            recipient_list = [usermail]
            send_mail(subject, message, from_email, recipient_list, fail_silently=False)
            return redirect('orders')
        else:
            messages.error(request, "Upload payments screenshot to proceed.")
            return redirect(banktransfer, card)

    context = {"card": order, "year": year}
    return render(request, "banktransfer.html", context)




@login_required(login_url="login")
def orders(request):
    year = datetime.datetime.now().year
    order = User_orders.objects.filter(user=request.user)

    return render(request, "orders.html", {"order":order, "year":year})


@login_required(login_url="login")
def del_order(request, card):
    order = User_orders.objects.get(id=card)
    order.delete()
    return redirect("orders")



@login_required(login_url="login")
def terms(request):
    year = datetime.datetime.now().year


    return render(request, "term.html", {"year":year})
