from django import forms
from django.db.models import fields
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = "__all__"
        labels = {
            "user_name" : "Your Name",
            "comment_text" : "Your Comment"
        }
