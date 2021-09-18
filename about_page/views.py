from django.shortcuts import render

# Create your views here.
def show_about_page(request):
    return render(request, "about_page/about_page.html")