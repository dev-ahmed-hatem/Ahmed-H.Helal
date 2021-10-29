from django.urls import path
from . import views

app_name = "store"
urlpatterns = [
    path("", views.home, name="home"),
    path("products/", views.products, name="products"),
    path("product/<int:productID>/", views.product, name="product"),
    path("seller/<int:sellerID>/", views.seller, name="seller"),
    path("about/", views.about, name="about"),
    path("cart/", views.cart, name="cart"),
    path("testimonial/", views.testimonial, name="testimonial"),
    path("why/", views.why, name="why"),
    path("checkout/", views.checkout, name="checkout"),
    path("update_cart/", views.updateCart, name="update_cart"),
    path("new_order/", views.newOrder, name="new_order"),
    path("shipping_order/<int:shippingID>", views.shippingOrder, name="shipping_order"),
    path("orders/", views.orders, name="orders"),
    path("confirm_order/<int:shippingID>", views.confirmOrder, name="confirm_order"),
    path("register/", views.register, name="register"),
    path("register_check/<str:registration_type>/", views.register_check, name="register_check"),
    path("logout/", views.logout_, name="logout"),
]
