#food/forms.py
from django import forms

from .models import Food

class PostForm(forms.ModelForm):

    class Meta:
        model = Food
        fields = ('', 'text',)