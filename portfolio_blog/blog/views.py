from django.shortcuts import render,reverse,get_object_or_404,redirect
from django.http import HttpResponseRedirect,HttpResponse
from django.views.generic import (TemplateView,CreateView,ListView,
                                  DetailView,UpdateView,DeleteView)
from blog.forms import userForm, profileForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from blog.forms import postForm, commentForm
from blog.models import Post, Comment
from django.utils import timezone
from django.urls import reverse_lazy
# Create your views here.

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = userForm(data=request.POST)
        profile_form = profileForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = userForm()
        profile_form = profileForm()
    return render(request,'registration/register.html',{'user_form':user_form,
                                                        'profile_form':profile_form,
                                                        'registered':registered})

def userLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username, password = password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('postList'))
            else:
                return HttpResponse('User is Not Active !')
        else:
            return HttpResponse('Invalid Login Credentials!')
    else:
        return render(request,'registration/login.html',{})

@login_required
def userLogout(request):
    logout(request)
    return HttpResponseRedirect(reverse('postList'))

class base(TemplateView):
    template_name = 'blog/base.html'

class postList(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

class postDraftList(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('created_date')

class postDetail(DetailView):
    model = Post

class postCreate(CreateView):
    model = Post
    form_class = postForm

class postUpdate(UpdateView):
    model = Post
    form_class = postForm

class postDelete(DeleteView):
    model = Post
    success_url = reverse_lazy('postList')

def postPublish(request,pk):
    post = get_object_or_404(Post,pk=pk)
    post.publish()
    return redirect('postDetail',pk=post.pk)


def addComment(request,pk):
    post = get_object_or_404(Post,pk=pk)
    if request.method == 'POST':
        form = commentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('postDetail',pk=post.pk)
    else:
        form = commentForm()
    return render(request,'blog/comment_form.html',{'form':form})

def approveComment(request,pk):
    comment = get_object_or_404(Comment,pk=pk)
    comment.approve()
    return redirect('postDetail',pk=comment.post.pk)

def deleteComment(request,pk):
    comment = get_object_or_404(Comment,pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('postDetail',pk=post_pk)