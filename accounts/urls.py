from django.conf.urls import url
from accounts import views as local_views

urlpatterns = [
	# Session login
    url(r'^signup/$', local_views.signup),
    url(r'^login/$', local_views.login_user),
    url(r'^logout/$', local_views.logout),
]
