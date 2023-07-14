from django.urls import path

from sayt.views import *

urlpatterns = [
    path("", index, name="home"),
    path("contact/", contact, name="contact"),
    path("shop/", shop, name="shop"),
    path("testimonial/", testimonial, name="testimonial"),
    path("why/", why, name="why"),
]
