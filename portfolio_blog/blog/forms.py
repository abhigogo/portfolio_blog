from django import forms
from django.contrib.auth.models import User
from blog.models import userProfile, Post, Comment

class userForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('username','email','password')

class profileForm(forms.ModelForm):
    class Meta:
        model = userProfile
        fields = ('profile_url',)

class postForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','text')

class commentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author','text')