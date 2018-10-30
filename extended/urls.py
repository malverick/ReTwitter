from django.conf.urls import url, include
from extended import views
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    url(r'^follow/', views.follow),
    url(r'^unfollow/', views.unfollow),
    url(r'^getUsers/', views.getUsers),
    url(r'^create/', views.createTweet),
    url(r'^delete/', views.deleteTweet),
    url(r'^read/', views.readTweet),

]
