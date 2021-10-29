from django.contrib import admin
from .models import *
from django.contrib.auth.models import User, Group
from django.contrib.sites.models import Site

# Register your models here.

# admin.site.unregister(User)
# admin.site.unregister(Group)
# admin.site.unregister(Site)


class ProductAdmin(admin.StackedInline):
    model = Product
    extra = 0


class SellerAdmin(admin.ModelAdmin):
    inlines = [ProductAdmin]


admin.site.register(Customer)
admin.site.register(DeliveryMan)
admin.site.register(Seller, SellerAdmin)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Offer)
admin.site.register(Shipping)
