from django.conf.urls import url, include
from accounts import views
from django.views.decorators.csrf import csrf_exempt
urlpatterns = [
    url(r'^signup/', views.signup),
    url(r'^login/$', views.Login_user),
    url(r'^logout/$', views.Logout),
]
