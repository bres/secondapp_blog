from django.urls import path
from . import views

app_name='blog'

urlpatterns =[
        path('',views.index,name='home'),
        path('posts/',views.postList,name='postlist'),
        path('<slug:slug>/',views.postSingle,name='postsingle')
        
        ]

