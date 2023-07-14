from django.shortcuts import render

from sayt.models import Product, Email, Contact


# Create your views here.


def index(requests):
    ctx = {}
    product = Product.objects.all().order_by('-pk')
    if requests.POST:
        if "email" in requests.POST:
            email = requests.POST.get('email')
            Email.objects.create(
                email=email
            )

        name = requests.POST.get('name')
        message = requests.POST.get('message')
        phone = requests.POST.get('phone')
        email = requests.POST.get('email')
        Contact.objects.create(
            name=name, message=message, phone=phone, email=email
        )
    ctx = {
        'products': product,
        "contact": contact
    }
    return render(requests, "index.html", ctx)


def contact(requests):
    ctx = {}
    if requests.POST:
        name = requests.POST.get('name')
        message = requests.POST.get('message')
        phone = requests.POST.get('phone')
        email = requests.POST.get('email')
        Contact.objects.create(
            name=name, message=message, phone=phone, email=email
        )

        ctx = {
            "contact": contact,

        }
    return render(requests, "contact.html", ctx)


def shop(requests):
    ctx = {}
    product = Product.objects.all().order_by('-pk')
    ctx = {
        'products': product,
    }
    return render(requests, "shop.html", ctx)


def testimonial(requests):
    ctx = {}
    if requests.POST:
        email = requests.POST.get('email')
        Email.objects.create(
            email=email
        )
        ctx = {
            "email": email
        }
    return render(requests, "testimonial.html", ctx)


def why(requests):
    ctx = {}
    if requests.POST:
        email = requests.POST.get('email')
        Email.objects.create(
            email=email
        )
        ctx = {
            "email": email
        }
    return render(requests, "why.html", ctx)