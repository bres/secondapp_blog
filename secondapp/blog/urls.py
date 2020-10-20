from django.urls import path
from . import views

app_name='blog'

urlpatterns =[
        path('',views.index,name='home'),
        path('posts/',views.postList,name='postlist'),
        path('post/<slug:slug>/',views.postSingle,name='postsingle'),
        path('new/',views.create_post, name='create_post'),
        path('update/<slug:slug>/',views.update_post,name='update_post'),
        path('delete/<slug:slug>/',views.delete_post,name='delete_post'),
        path('writers/', views.writersList, name='writerslist'),
        ]

