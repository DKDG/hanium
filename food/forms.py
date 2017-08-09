#food/forms.py
from django import forms
from .models import Restaurant

class PostModelForm(forms.ModelForm):

    class Meta:
        model = Restaurant
        fields = '__all__' 