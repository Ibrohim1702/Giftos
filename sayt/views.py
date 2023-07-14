from django.shortcuts import render

from sayt.models import Product, Email, Contact


# Create your views here.


def index(requests):
    ctx = {}
    product = Product.objects.all().order_by('-pk')
    if requests.POST:
        email = requests.POST.get('email')
        Email.objects.create(
            email=email
        )
    if requests.POST:
        name = requests.POST.get('name')
        message = requests.POST.get('message')
        phone = requests.POST.get('phone')
        email = requests.POST.get('email')
        Contact.objects.create(
            name=name, message=message, phone=phone, email=email
        )
        ctx = {
            "email": email,
            'products': product,
            "contact": contact
        }
    return render(requests, "index.html", ctx)


def contact(requests):
    ctx = {

    }
    return render(requests, "contact.html", ctx)


def shop(requests):
    ctx = {

    }
    return render(requests, "shop.html", ctx)


def testimonial(requests):
    ctx = {

    }
    return render(requests, "testimonial.html", ctx)


def why(requests):
    ctx = {

    }
    return render(requests, "why.html", ctx)