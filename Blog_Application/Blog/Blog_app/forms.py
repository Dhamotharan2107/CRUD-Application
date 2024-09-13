from django import forms
from .models import Blogs

class BlogsForm(forms.ModelForm):
    class Meta:
        model = Blogs
        fields = "__all__"
        # exclude = ['title','tags'] --- for not spefic fields