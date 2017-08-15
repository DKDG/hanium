from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
# Create your models here.
'''
# Restaurant
- author / CharField : 작성자
- title/ CharField : 식당 이름
- tag / CharField : 식당 관련 태그
- location / CharField : 주소
- food_image / URLField : 음식사진url
- res_image / URLField : 식당사진url
- opentime / TextField : 영업시간
- menuinfo / TextField : 메뉴
- created_at / DateTimeField / 작성시간
- updated_at / DateTimeField / 수정시간
'''

def min_length_3(value):
    if len(value) < 3:
        raise ValidationError('3글자 이상 입력해주세요.')

class Restaurant(models.Model):
    author = models.CharField(max_length=20, help_text='포스팅 작성자 이름을 입력해주세요.')
    title = models.CharField(max_length=100, validators=[min_length_3], help_text='제목을 3글자 이상 입력하세요')
    tag = models.CharField(max_length=50, help_text='관련 태그를 입력하세요')  
    location = models.CharField(max_length=50, help_text='도로명 주소를 입력하세요.')  
    food_image = models.URLField(help_text='음식사진 URL을 입력하세요.') 
    res_image = models.URLField(help_text='식당 사진 URL을 입력하세요.') 
    opentime = models.TextField(help_text='영업시간을 입력하세요.') 
    menuinfo = models.TextField(help_text='메뉴를 입력하세요.') 
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True) 

    class Meta:
       ordering = ['-id']
       
    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Restaurant)
    author = models.CharField(max_length = 10)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

