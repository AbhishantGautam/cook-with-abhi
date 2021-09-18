from django.urls import path
from . import views

urlpatterns = [
    path("", views.show_about_page, name="about_page")
]