# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Follows, Tweets
# Register your models here.

class FollowData(admin.ModelAdmin):
    list_display = ('follower', 'following')

admin.site.register(Follows, FollowData)


class TweetsData(admin.ModelAdmin):
    list_display = ('username', 'tweet')

admin.site.register(Tweets, TweetsData)
