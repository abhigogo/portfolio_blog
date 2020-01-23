from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.shortcuts import redirect
from django.urls import reverse

# Create your models here.
class userProfile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    profile_url = models.URLField()

class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now())
    published_date = models.DateTimeField(blank=True,null=True)

    def get_absolute_url(self):
        return reverse('postDetail',kwargs={'pk':self.pk})

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approve_comments(self):
        return self.comments.filter(approved_comment = True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey('blog.Post',related_name='comments',on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now())
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def get_absolute_url(self):
        return reverse('postList')

    def __str__(self):
        return self.text