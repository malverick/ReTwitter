from django.conf.urls import url
from extended import views

urlpatterns = [
    url(r'^follow/$', views.follow),
    url(r'^unfollow/$', views.unfollow),
    url(r'^getUsers/$', views.getUsers),
    url(r'^create/$', views.createTweet),
    url(r'^delete/$', views.deleteTweet),
    url(r'^read/$', views.readTweet),
]
