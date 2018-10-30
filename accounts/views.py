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

# Create your views here.
import json

@api_view(['POST'])
def signup(request):
    """
    This method is used for user registration. Username should be unique.
    Password should be atleast 8 characters and should include a number.
    """
    if request.method == 'POST':
        username = request.data["username"]
        password = request.data["password"]
        if not User.objects.filter(username=username).exists():
            user = User.objects.create(username = username, password = password)
            user.save()
            user = User.objects.get(username=username)
            user.set_password(password)
            user.save()
            login(request, user)
            return JsonResponse({"Note":"User successfully logged in"})
        return JsonResponse({"Note":"User already exist"})

@api_view(['POST'])
def Login_user(request):
    """
    This method is used for user login.
    """
    if request.method == 'POST':
        username = request.data["username"]
        password = request.data["password"]
        user = authenticate(username = username, password = password)
        if user is not None:
            login(request, user)
        else:
            return JsonResponse({"Error":"Invalid username or password"})
        return JsonResponse({"Note":"User successfully logged in"})

@api_view(['GET'])
def Logout(request):
    """
    This method is used for user logout.
    """
    logout(request)
    return JsonResponse({"Note":"Successfully logged out"})
