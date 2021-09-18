from django.shortcuts import render
from .forms import ReviewForm
from django.http.response import HttpResponseRedirect
from .models import Review


# Create your views here.
def show_review(request):
    form = ReviewForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            review = Review(username = form.cleaned_data["username"], text = form.cleaned_data["text"])
            review.save()
            return HttpResponseRedirect("/review")
    all_reviews = Review.objects.all()
    return render(request, "review/review.html", {
        "form" : form,
        "reviews" : all_reviews
    })