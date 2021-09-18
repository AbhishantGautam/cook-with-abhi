from django.urls import path
from . import views

urlpatterns=[
    path("", views.show_review, name="review_page")
]