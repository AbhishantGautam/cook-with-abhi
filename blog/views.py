from blog.forms import CommentForm
from django.forms.forms import Form
from django.http.response import HttpResponse, HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render
from .models import Post,Comment
from random import randint
from .forms import CommentForm

# Create your views here.
def show_all_blogs(request):
    all_posts = Post.objects.all()
    return render(request, "blog/homepage_blog.html", {
        "all_posts" : all_posts 
    })

posts_ = Post.objects.all()
post_list = []
for post_ in posts_ :
    post_list.append(post_)


def show_blog_page(request, blog_name):
    def increment(self):
        return self+1
    form = CommentForm(request.POST)
    if request.method == "POST":
        
        if form.is_valid():
            comment = Comment(user_name = form.cleaned_data["user_name"], comment_text = form.cleaned_data["comment_text"])
            comment.save()
            return HttpResponseRedirect("/about-cook")
    all_posts = Post.objects.all()
    selected_posts=[]
    for i in range(0,4):
        random_num = randint(0, (len(all_posts)))
        selected_posts.append(all_posts[abs(random_num - 1)])
    post = Post.objects.get(slug = blog_name)
    return render(request, "blog/individual_blogs_page.html", {
        "post" : post,
        "selected_posts" : selected_posts,
        "i" : 1,
        "form" : form
    })


