from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=60)
    phone = models.CharField(max_length=40)
    email = models.EmailField()

    def __unicode__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=60)
    price = models.CharField(max_length=60)
    description = models.TextField()
    type = models.CharField(max_length=60)
    number = models.IntegerField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name


class Purchase(models.Model):
    name = models.CharField(max_length=60, blank=True)
    email = models.EmailField(blank=True)
    phone_number = models.CharField(max_length=10, blank=True)
    product = models.ForeignKey(Product)
    quantity = models.IntegerField(null=True, blank=True)
    date = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.product

