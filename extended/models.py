# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Follows(models.Model):
    """
    Database schema for followers/following.
    'follower' represents the username who follows.
    'following' represents the username who is followed by.
    Example: follower = 'username1'
             following = 'username2'
             username1 follows username2
    """
    follower = models.TextField()
    following = models.TextField()


class Tweets(models.Model):
    """
    Database schema for tweets.
    'username' represents the owner of the tweet.
    'tweet' represent the content of the tweet.
    """
    username= models.TextField()
    tweet = models.TextField(max_length=280)
