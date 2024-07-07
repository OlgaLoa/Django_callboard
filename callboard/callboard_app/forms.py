from django import forms
from django.core.exceptions import ValidationError
from django_summernote.fields import SummernoteTextField

from .models import Post

class PostForm(forms.ModelForm):
   text = SummernoteTextField()

   class Meta:
        model = Post
        fields = [
            'author',
            'title',
            'category',
            'text',
        ]
