from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phone = PhoneNumberField(null=True)
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class DeliveryMan(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = PhoneNumberField(null=True)

    class Meta:
        verbose_name = "Delivery Man"
        verbose_name_plural = "Delivery Men"

    def __str__(self):
        return self.name


class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    details = models.TextField(max_length=5000)
    phone = PhoneNumberField(null=True)
    img = models.ImageField(upload_to="store/images/products")

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    price = models.FloatField("Price")
    details = models.TextField()
    img = models.ImageField(upload_to="store/images/products", default="store/images/products/product.png")

    def __str__(self):
        return self.name


class Offer(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    start = models.DateTimeField("Date Start", auto_now_add=True)
    end = models.DateTimeField("Date End")

    def __str__(self):
        return "offer " + str(self.id)


class Cart(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)

    @property
    def total_quantity(self):
        total = sum([item.quantity for item in self.cartitem_set.all()])
        return total

    @property
    def total_price(self):
        total = sum([item.total_price for item in self.cartitem_set.all()])
        return total

    def __str__(self):
        return f"{self.user.name}'s cart"


class CartItem(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    date_added = models.DateTimeField("Date Added", auto_now_add=True)

    @property
    def total_price(self):
        total = self.product.price * self.quantity
        return total


class Shipping(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    delivery_man = models.ForeignKey(DeliveryMan, on_delete=models.CASCADE, null=True)
    order = models.OneToOneField(Cart, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200, default="")
    email = models.CharField(max_length=200, default="")
    address = models.CharField(max_length=200, default="")
    city = models.CharField(max_length=200, default="")
    phone = models.CharField(max_length=200, default="")
    date_ordered = models.DateTimeField("Date Ordered", auto_now_add=True)
    status = models.CharField(
        max_length=10,
        choices=[
            ("ordered", "Ordered"),
            ("confirmed", "Confirmed"),
            ("delivered", "Delivered"),
            ("canceled", "Canceled"),
            ],
        default="ordered"
    )

    def __str__(self):
        return f"order: {self.id}, {self.order}, {self.address}"
