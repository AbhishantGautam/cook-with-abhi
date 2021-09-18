from django.shortcuts import render
from blog.models import Post
from menu.models import Recipe


# Create your views here.

def show_homepage (request):
    all_blogs = Post.objects.all()
    all_recipes = Recipe.objects.all()
    return render (request, "homepage/homepage.html", {
        "blogs" : all_blogs,
        "recipes" : all_recipes,
        
    })