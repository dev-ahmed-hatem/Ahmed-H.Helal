import json
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from .models import *
from django.shortcuts import get_object_or_404

# Create your views here.


def register(request):
    if request.user.is_authenticated:
        return redirect("store:home")
    else:
        return render(request, "store/register.html")


def register_check(request, registration_type):
    if not request.user.is_authenticated:
        if registration_type == "login":
            return loginValidation(request)
        else:
            return signupValidation(request)
    else:
        return redirect("store:home")


def loginValidation(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    login_error = None
    loginUsername = None
    try:
        login_error = "Username not found!"
        User.objects.get(username=username)
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect("store:home")
        else:
            login_error = "Password is incorrect!"
            loginUsername = username
            raise Exception()

    except Exception as e:
        print(e)
        context = {
            "login_error": login_error,
            "login_username": loginUsername
        }
        return render(request, "store/register.html", context)


def signupValidation(request):
    firstName = request.POST.get("first name")
    lastName = request.POST.get("last name")
    username = request.POST.get("username")
    email = request.POST.get("email")
    address = request.POST.get("address")
    phone = request.POST.get("phone")
    city = request.POST.get("city")
    password = request.POST.get("password")
    confirmPassword = request.POST.get("confirm password")
    signup_error = None

    try:
        users = User.objects.filter(username=username)
        if len(users) > 0:
            signup_error = "Username not available!"
            raise Exception()
        if password != confirmPassword:
            signup_error = "Passwords aren't identical!"
            raise Exception()

        # create new user
        newUser = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=firstName,
            last_name=lastName
        )
        # create new customer
        Customer.objects.create(
            user=newUser,
            name=f"{newUser.first_name.strip().title()} {newUser.last_name.strip().title()}",
            address=address,
            phone=phone,
            city=city
        )
        # log user in
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect("store:home")

    except Exception as e:
        print(e)
        context = {
            "signup": True,
            "signup_error": signup_error,
            "signup_first_name": firstName,
            "signup_last_name": lastName,
            "signup_email": email,
            "signup_address": address,
            "signup_phone": phone,
            "signup_city": city,
        }
        return render(request, "store/register.html", context)


def logout_(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect("store:register")


@login_required(login_url="/store/register/")
def home(request):
    items = Product.objects.all()
    offers = Offer.objects.all()
    context = {"items": items, "offers": offers}
    return render(request, "store/home.html", context)


def products(request):
    items = Product.objects.all()
    context = {"items": items}
    return render(request, "store/products.html", context)


def product(request, productID):
    item = get_object_or_404(Product, id=productID)
    context = {"item": item}
    return render(request, "store/product.html", context)


def seller(request, sellerID):
    shop = get_object_or_404(Seller, id=sellerID)
    context = {"seller": shop}
    return render(request, "store/seller.html", context)


def about(request):
    return render(request, "store/about.html")


@login_required(login_url="/store/register/")
def cart(request):
    user = request.user.customer
    try:
        newCart = Cart.objects.get(user=user, ordered=False)
    except Exception as e:
        print(e)
        newCart = None

    try:
        shipping_orders = Shipping.objects.filter(user=user)
    except Exception as e:
        print(e)
        shipping_orders = []
    context = {"newCart": newCart, "shipping_orders": shipping_orders}
    return render(request, "store/cart.html", context)


def testimonial(request):
    return render(request, "store/testimonial.html")


def why(request):
    return render(request, "store/why.html")


@login_required(login_url="/store/register/")
def checkout(request):
    order = Cart.objects.all().get(user=request.user.customer, ordered=False)
    context = {"usercart": order}
    return render(request, "store/checkout.html", context)


@login_required(login_url="/store/register/")
def orders(request):
    shipping = Shipping.objects.filter(status="ordered")
    confirmed_shipping = Shipping.objects.exclude(status="ordered")
    context = {"shipping": shipping, "confirmed_shipping": confirmed_shipping}
    return render(request, "store/shipping.html", context)


@login_required(login_url="/store/register/")
def shippingOrder(request, shippingID):
    shipping = Shipping.objects.get(id=shippingID)
    context = {"shipping": shipping}
    return render(request, "store/shipping_order.html", context)


@login_required(login_url="/store/register/")
def updateCart(request):
    user = request.user.customer
    order, created = Cart.objects.get_or_create(user=user, ordered=False)
    data = json.loads(request.body)
    productID = data["productID"]
    quantity = data["quantity"]
    action = data["action"]

    if action == "add-item":
        item, created = CartItem.objects.get_or_create(user=user, cart=order, product_id=productID)
        item.quantity = quantity
        item.save()
    elif action == "remove-item":
        item = CartItem.objects.get(user=user, cart=order, product_id=productID)
        item.delete()
        if order.cartitem_set.count() <= 0:
            order.delete()
    elif action == "remove-cart":
        order.delete()

    return HttpResponse("cart updated successfully")


@login_required(login_url="/store/register/")
def newOrder(request):
    user = request.user.customer
    order = Cart.objects.get(user=user, ordered=False)
    order.ordered = True
    order.save()

    data = request.POST
    name = data.get("name")
    email = data.get("email")
    address = data.get("address")
    city = data.get("city")
    phone = data.get("phone")
    shipping = Shipping(
        user=user,
        order=order,
        name=name,
        email=email,
        address=address,
        city=city,
        phone=phone
    )
    shipping.save()
    return cart(request)


@login_required(login_url="/store/register/")
def confirmOrder(request, shippingID):
    user = request.user.deliveryman
    shipping = Shipping.objects.get(id=shippingID)
    shipping.delivery_man = user
    shipping.status = "confirmed"
    shipping.save()
    return shippingOrder(request, shippingID)
