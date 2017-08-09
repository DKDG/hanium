from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.main, name='main'),
    url(r'^/about$', views.about, name='about'),
    url(r'^/service$', views.service, name='service'),
    url(r'^/contact$', views.contact, name='contact'),
    # url(r'^(?P<pk>\d+)/$', views.post_detail, name='post_detail'),

]
   
   #url(r'^(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
   # url(r'^new/$', views.post_new, name='post_new'),