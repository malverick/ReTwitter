# -*- coding: utf-8 -*-
from __future__ import unicode_literals

#from django.shortcuts import render
#from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
#from django.http import JsonResponse, HttpResponse
#from django.contrib.auth import authenticate
from django.contrib.auth.models import User
#from django.contrib.auth import views as auth_views
from django.views.decorators.csrf import csrf_exempt
from models import Follows, Tweets
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
import json

@csrf_exempt
@api_view(['POST'])
@permission_classes((IsAuthenticated,))      
def follow(request):
    """
    This method is used to follow a particular user.
    'request.user' represents username of logged in user.
    'request.body' contains username of person in JSON format
    who is to be followed.
    """
    to_follow = request.data.get("follow")
    if to_follow is None:
        return Response({'error':'Please provide username to be followed with key follow'},
                        status=HTTP_400_BAD_REQUEST)
    
    if str(to_follow) == str(request.user):
        return Response({'Error':'You cannot follow/unfollow yourself'},
                        status=HTTP_400_BAD_REQUEST)
    l = User.objects.filter(username = to_follow).first()
    if l is None:
        return Response({'Error':'The user you wish to follow does not exist.'},
                            status=HTTP_400_BAD_REQUEST)
    obj = Follows.objects.filter(follower = request.user, following = str(l.username))
    if len(obj) == 0:
        user = Follows(follower = request.user, following = str(l.username))
        user.save()
        note  = 'Follow request Successfull. ' + str(request.user) + ' started following  ' + str(l.username)
        return Response({'Note': note}, status=HTTP_200_OK)
    else:
        return Response({'Error': 'You are already following this user'}, status=HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['POST'])
@permission_classes((IsAuthenticated,))      
def unfollow(request):
    """
    This method is used to unfollow a particular user.
    'request.user' represents username of logged in user.
    'request.body' contains username of person in JSON format
    who is to be unfollowed.
    """
    to_unfollow = request.data.get("unfollow")
    if to_unfollow is None:
        return Response({'error':'Please provide username to be unfollowed with key unfollow'},
                        status=HTTP_400_BAD_REQUEST)
    
    if str(to_unfollow) == str(request.user):
        return Response({'Error':'You cannot follow/unfollow yourself'},
                        status=HTTP_400_BAD_REQUEST)
    
    l = User.objects.filter(username = to_unfollow).first()
    if l is None:
        return Response({'Error':'The user you wish to unfollow does not exist.'},
                        status=HTTP_400_BAD_REQUEST)
    obj = Follows.objects.filter(follower = request.user, following = str(l.username))
    if len(obj) != 0:
        obj.delete()
        return Response({'Note': 'Unfollow request Successfull'}, status=HTTP_200_OK)
    else:
        return Response({'Error': 'You are not following this user, unfollow request not possible.'},
                        status=HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['GET'])
@permission_classes((IsAuthenticated,))      
def getUsers(request):
    """
    This method is used to display the list of all registered
    users mentioning their 'userId' and 'username'.
    """
    user = User.objects.all()
    dict = {}
    for i in user:
        dict[i.id] = i.username
    return Response(dict, status=HTTP_200_OK)

@csrf_exempt
@api_view(['POST'])
@permission_classes((IsAuthenticated,))      
def createTweet(request):
    """
    This method is used to create a tweet by a logged in user.
    'request.user' represents username of logged in user.
    'request.body' contains tweet in JSON format which the user
    wants to create.
    """
    to_tweet = request.data.get("tweet")
    if to_tweet is None:
        return Response({'error':'Please provide content of tweet to create with key tweet'},
                        status=HTTP_400_BAD_REQUEST)
    tweet = Tweets(username = request.user, tweet = str(to_tweet))
    tweet.save()
    obj = Tweets.objects.filter(username = request.user, tweet = str(to_tweet)).last()
    note = "Tweet Creation Successfull, with Tweet ID " + str(obj.id)
    return Response({'Note': note}, status=HTTP_200_OK)

@csrf_exempt
@api_view(['POST'])
@permission_classes((IsAuthenticated,))      
def deleteTweet(request):
    """
    This method is used to delete a tweet created by a logged in user.
    'request.user' represents username of logged in user.
    'request.body' contains tweetID in JSON format which the user
    wants to delete.
    """
    to_delete = request.data.get("tweetID")
    if to_delete is None:
        return Response({'error':'Please provide ID of tweet to delete with key tweetID'},
                        status=HTTP_400_BAD_REQUEST)
    l = Tweets.objects.filter(id = str(to_delete)).first()
    if l is None:
        return Response({'Error':'No such Tweet exists'}, status=HTTP_400_BAD_REQUEST)
    obj = Tweets.objects.filter(id = str(to_delete), username=request.user)
    if len(obj) != 0:
        obj.delete()
        return Response({'Note': 'Tweet Successfully deleted'}, status=HTTP_200_OK)
    else:
        return Response({'Error': 'You are not authorized to delete this tweet.'})

@csrf_exempt
@api_view(['POST'])
@permission_classes((IsAuthenticated,))      
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
    to_read_user = request.data.get("username")
    to_read_id = request.data.get("tweetID")
    if to_read_user is None or str(to_read_user) == "":
        to_read_user = request.user
    l = User.objects.filter(username = str(to_read_user)).first()
    if l is None:
        return Response({'Error':'No such user exists'}, status=HTTP_400_BAD_REQUEST)

    if to_read_id is None or str(to_read_id) == "":
        chk = Tweets.objects.filter(username = str(to_read_user))
        k = {}
        for i in chk:
            k[i.id] = i.tweet
        return Response(k, status=HTTP_200_OK)
    else:
        chk = Tweets.objects.filter(id = int(to_read_id), username = str(to_read_user))
        if len(chk) != 0:
            k = {}
            for i in chk:
                k[i.id] = i.tweet
            return Response(k, status=HTTP_200_OK)
        else:
            return Response({'Error':'No such Tweet exists'}, status=HTTP_200_OK)
