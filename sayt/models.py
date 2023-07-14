from django.db import models
from django.utils.text import slugify
# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=128)
    price = models.CharField(max_length=128)
    img = models.ImageField()


    def save(self, *args, **kwargs):
        if not self.key:
            self.key = slugify(self.name)
        return super(Product, self).save(*args, **kwargs)
    def __str__(self):
        return self.name

class Email(models.Model):
    email = models.CharField(max_length=128)
    def __str__(self):
        return self.email




class Contact(models.Model):
    name = models.CharField(max_length=128)
    email = models.CharField(max_length=128)
    phone = models.CharField(max_length=128)
    message = models.CharField(max_length=128)

    def __str__(self):
        return self.name