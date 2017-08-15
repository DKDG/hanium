#food/forms.py
from django import forms
from .models import Restaurant, Comment

''' author = models.CharField(max_length=20, help_text='포스팅 작성자 이름을 입력해주세요.')
    title = models.CharField(max_length=100, validators=[min_length_3], help_text='제목을 3글자 이상 입력하세요')
    tag = models.CharField(max_length=50, help_text='관련 태그를 입력하세요')  
    location = models.CharField(max_length=50, help_text='도로명 주소를 입력하세요.')  
    food_image = models.URLField(help_text='음식사진 URL을 입력하세요.') 
    res_image = models.URLField(help_text='식당 사진 URL을 입력하세요.') 
    opentime = models.TextField(help_text='영업시간을 입력하세요.') 
    menuinfo = models.TextField(help_text='메뉴를 입력하세요.') 
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True) 
'''
class PostModelForm(forms.ModelForm):

    class Meta:
        model = Restaurant
        fields = '__all__' 


class CommentModelForm(forms.ModelForm):

    class Meta:
        model = Comment
        #fields = '__all__'
        fields = ('author', 'message')