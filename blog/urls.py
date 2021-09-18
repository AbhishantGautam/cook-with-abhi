from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.show_all_blogs, name="blog_homepage"),
    path("<blog_name>", views.show_blog_page, name="blog_detailpage"),
] 
