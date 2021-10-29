from django.urls import path
from . import views


app_name = "tracker"
urlpatterns = [
    path("main-page/", views.main_page, name="main-page"),
]
