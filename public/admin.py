from django.contrib import admin
from models import Product, Purchase, UserProfile


# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email')
    search_fields = ('name', 'phone', 'email')
    list_filter = ['phone']


class ProductAdmin(admin.ModelAdmin):
    list_display = ('price', 'name', 'type', 'number', 'updated')
    search_fields = ('price', 'name', 'type', 'number', 'updated')
    list_filter = ['price', 'name', 'type', 'number', 'updated']


class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('product', 'name', 'email', 'phone_number', 'quantity', 'date')
    search_fields = ('product', 'name', 'email', 'phone_number', 'quantity', 'date')
    list_filter = ['product', 'name', 'email', 'phone_number', 'quantity', 'date']


# admin.site.register(UserProfile, UserProfile)
admin.site.register(Product, ProductAdmin)
admin.site.register(Purchase, PurchaseAdmin)
