# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse, HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth import views as auth_views
from django.views.decorators.csrf import csrf_exempt
import json
from models import Follows, Tweets
# Create your views here.

@csrf_exempt
def follow(request):
    """
    This method is used to follow a particular user.
    'request.user' represents username of logged in user.
    'request.body' contains username of person in JSON format
    who is to be followed.
    """
    if request.method == 'POST':
        if str(request.user) == "AnonymousUser":
            return JsonResponse({"Error":"Login First"})
        d={}
        d = json.loads(request.body)
        l = User.objects.filter(username = d["follow"]).first()
        if l is None:
            return JsonResponse({"Error":"No such user exists"})
        obj = Follows.objects.filter(follower = request.user, following = str(l.username))
        if len(obj) == 0:
            user = Follows(follower = request.user, following = str(l.username))
            user.save()
            note  = "Follow request Successfull. " + str(request.user) + " started following  " + str(l.username)
            return JsonResponse({"Note": note})
        else:
            return JsonResponse({"Error": "You are already following this user"})
    else:
        return JsonResponse({"Error": "Make sure your request method is POST"})

@csrf_exempt
def unfollow(request):
    """
    This method is used to unfollow a particular user.
    'request.user' represents username of logged in user.
    'request.body' contains username of person in JSON format
    who is to be unfollowed.
    """
    if request.method == 'POST':
        if str(request.user) == "AnonymousUser":
            return JsonResponse({"Error":"Login First"})
        d={}
        d = json.loads(request.body)
        l = User.objects.filter(username = d["unfollow"]).first()
        if l is None:
            return JsonResponse({"Error":"No such user exists"})
        obj = Follows.objects.filter(follower = request.user, following = d["unfollow"])
        if len(obj) != 0:
            obj.delete()
            return JsonResponse({"Note": "Unfollow request Successfull"})
        else:
            return JsonResponse({"Error": "You are not following this user, unfollow request not possible."})
    else:
        return JsonResponse({"Error": "Make sure your request method is POST"})

@api_view(['GET'])
def getUsers(request):
    """
    This method is used to display the list of all registered
    users mentioning their 'userId' and 'username'.
    """
    if request.method == 'GET':
        if str(request.user) == "AnonymousUser":
            return JsonResponse({"Error":"Login First"})
        user = User.objects.all()
        dict = {}
        for i in user:
            dict[i.id] = i.username
        return JsonResponse(dict)

@csrf_exempt
def createTweet(request):
    """
    This method is used to create a tweet by a logged in user.
    'request.user' represents username of logged in user.
    'request.body' contains tweet in JSON format which the user
    wants to create.
    """
    if request.method == 'POST':
        if str(request.user) == "AnonymousUser":
            return JsonResponse({"Error":"Login First"})
        d={}
        d = json.loads(request.body)
        tweet = Tweets(username = request.user, tweet = d["tweet"])
        tweet.save()
        obj = Tweets.objects.filter(username = request.user, tweet = d["tweet"]).last()
        note = "Tweet Creation Successfull, with Tweet ID " + str(obj.id)
        return JsonResponse({"Note": note})
    else:
        return JsonResponse({"Error": "Make sure your request method is POST"})

@csrf_exempt
def deleteTweet(request):
    """
    This method is used to delete a tweet created by a logged in user.
    'request.user' represents username of logged in user.
    'request.body' contains tweetID in JSON format which the user
    wants to delete.
    """
    if request.method == 'POST':
        if str(request.user) == "AnonymousUser":
            return JsonResponse({"Error":"Login First"})
        d={}
        d = json.loads(request.body)
        l = Tweets.objects.filter(id = d["tweetID"]).first()
        if l is None:
            return JsonResponse({"Error":"No such Tweet exists"})
        obj = Tweets.objects.filter(id = d["tweetID"], username=request.user)
        if len(obj) != 0:
            obj.delete()
            return JsonResponse({"Note": "Tweet Successfully deleted"})
        else:
            return JsonResponse({"Error": "You are not authorized to delete this tweet."})
    else:
        return JsonResponse({"Error": "Make sure your request method is POST"})

@csrf_exempt
def readTweet(request):
    """
    This method is used to read a tweet created by a particular user.
    'request.user' represents username of logged in user.
    'request.body' contains two parameters, 'username' and 'tweetID'.
    'username' in 'request.body' represents the user whose tweet is to be read.
    'tweetID' in 'request.body' represents the tweet ID of the tweet created
    by the 'username'.
    If the tweetID field is left empty, then the method displays all the tweets
    created the 'username'.
    """
    if request.method == 'POST':
        if str(request.user) == "AnonymousUser":
            return JsonResponse({"Error":"Login First"})
        d={}
        d = json.loads(request.body)
        l = User.objects.filter(username = d["username"]).first()
        if l is None:
            return JsonResponse({"Error":"No such user exists"})

        if d["tweetID"] == "":
            chk = Tweets.objects.filter(username = d["username"])
            k = {}
            for i in chk:
                k[i.id] = i.tweet
            return JsonResponse(k)
        else:
            chk = Tweets.objects.filter(id = d["tweetID"], username = d["username"])
            if len(chk) != 0:
                k = {}
                for i in chk:
                    k[i.id] = i.tweet
                return JsonResponse(k)
            else:
                return JsonResponse({"Error":"No such Tweet exists"})
    else:
        return JsonResponse({"Error": "Make sure your request method is POST"})
