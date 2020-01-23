from django.conf.urls import url
from blog import views

urlpatterns = [
    url(r'^$',views.postList.as_view(),name='postList'),
    url(r'^register',views.register,name='register'),
    url(r'^login',views.userLogin,name='login'),
    url(r'^logout',views.userLogout,name='logout'),
    url(r'^post/new/$',views.postCreate.as_view(),name='postCreate'),
    url(r'drafts/$',views.postDraftList.as_view(),name='postDrafts'),
    url(r'^post/(?P<pk>\d+)/$',views.postDetail.as_view(),name='postDetail'),
    url(r'post/(?P<pk>\d+)/edit/$',views.postUpdate.as_view(),name='postEdit'),
    url(r'post/(?P<pk>\d+)/remove/$',views.postDelete.as_view(),name='postRemove'),
    url(r'post/(?P<pk>\d+)/publish/$',views.postPublish,name='postPublish'),
    url(r'post/(?P<pk>\d+)/comment/$',views.addComment,name='addComment'),
    url(r'comment/(?P<pk>\d+)/approve/$',views.approveComment,name='approveComment'),
    url(r'comment/(?P<pk>\d+)/remove/$',views.deleteComment,name='deleteComment'),

]