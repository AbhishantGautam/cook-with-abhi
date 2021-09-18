from django.urls import path
from . import views
urlpatterns=[
    path("", views.show_menu, name="menu_page"),
    path("<slug:slug>", views.show_recipe, name="recipe_page")
]