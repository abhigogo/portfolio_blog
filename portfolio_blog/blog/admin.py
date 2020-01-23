from django.contrib import admin
from blog.models import userProfile, Post, Comment
# Register your models here.

admin.site.register(userProfile)
admin.site.register(Post)
admin.site.register(Comment)
