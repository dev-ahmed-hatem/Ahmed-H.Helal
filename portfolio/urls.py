from django.urls import path
from . import views


app_name = "portfolio"
urlpatterns = [
    path("about/", views.about, name="about"),
    path("skills/", views.skills, name="skills"),
    path("works/", views.works, name="works"),
    path("contact/", views.contact, name="contact"),
    path("fingers/", views.fingers, name="fingers"),
    path("downloader/", views.downloader, name="downloader"),
    path("rewriter/", views.rewriter, name="rewriter"),
]
