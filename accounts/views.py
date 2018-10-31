# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response

@csrf_exempt
@api_view(['POST'])
@permission_classes((AllowAny,))
def signup(request):
    """
    This method is used for user registration. Username should be unique.
    Password should be atleast 8 characters and should include a number.
    """
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error':'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    if not User.objects.filter(username=username).exists():
        user = User.objects.create(username = username, password = password)
        user.save()
        user = User.objects.get(username=username)
        user.set_password(password)
        user.save()
        user = authenticate(username = username, password = password)
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token':token.key}, status=HTTP_200_OK)
    return Response({'Note':'User already exist'}, status=HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['POST'])
@permission_classes((AllowAny,))
def login_user(request):
    """
    This method is used for user login.
    """
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error':'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username = username, password = password)
    if not user:
        return Response({'error':'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token':token.key}, status=HTTP_200_OK)

@csrf_exempt
@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def logout(request):
    """
    This method is used for user logout.
    """
    request.user.auth_token.delete()
    return Response({'Note':'Successfully logged out'}, status=HTTP_200_OK)
