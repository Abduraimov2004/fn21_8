from django.urls import path
from .views import index, about, contact, post, post1, post2, post3

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('post/', post, name='post'),
    path('post1/', post1, name='post1'),
    path('post2/', post2, name='post2'),
    path('post3/', post3, name='post3'),

]
