from django.shortcuts import render

from sayt.models import Product


# Create your views here.


def index(requests):
    product = Product.objects.all().order_by('-pk')
    ctx = {
        'products': product[1:],
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