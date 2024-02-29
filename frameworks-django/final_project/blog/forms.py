
from django import forms
from .models import Post

class SearchForm(forms.Form):
    keyword = forms.CharField()


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'category', 'image']