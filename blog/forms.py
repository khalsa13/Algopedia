from django import forms
from .models import Post


class SavePost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'image', 'explain', 'adv', 'disadv', 'similar',]

