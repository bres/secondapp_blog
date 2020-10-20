from django.forms import ModelForm, Textarea
from .models import Post

class PostForm(ModelForm):
    class Meta:
        model=Post
        fields=['title','slug','content','excerpt','status']
        widgets = {
            'excerpt': Textarea(attrs={'cols': 80, 'rows':3}),
            'content': Textarea(attrs={'cols': 80, 'rows':5}),

        }

