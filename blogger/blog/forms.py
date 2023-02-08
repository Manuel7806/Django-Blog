from django import forms
from django.utils.text import slugify
from .models import Post, Comments


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'body',
        ]

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title', 'required': True}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter your post here.', 'required': True})
        }
