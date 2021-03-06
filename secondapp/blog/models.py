from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here

class Post(models.Model):
   

    class NewManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status="published")




    options=(
            ('draft','Draft'),
            ('published','Published'),
            )

    excerpt=models.TextField(default="put a part of your contente here")
    title=models.CharField(max_length=250)
    slug=models.SlugField(max_length=250,unique_for_date='publish')
    publish=models.DateTimeField(default=timezone.now)
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name='blog_posts')
    content=models.TextField()
    status=models.CharField(max_length=10,choices=options,default='draft')
    objects=models.Manager() #default manager
    newmanager=NewManager() #custom manager

    class Meta:
        ordering = ('-publish',)


    def __str__(self):
        return self.title

   



