from django import forms
from django.forms import fields
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = "__all__"
        labels = {
            "username" : "Your name",
            "text" : "comment",
        }