from django import forms
from .models import BlogPost


class PostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'short_description', 'content', 'media']
        widgets = {
             "title" : forms.TextInput(),
            "short_description": forms.Textarea( ),
            "content": forms.Textarea(),
            "media" : forms.ClearableFileInput(),
        }

   
