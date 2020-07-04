from django.shortcuts import render
from myapp.models import ActivityPeriod, User
from myapp.serializers import UserSerializer, ActivityPeriodSerializer
from rest_framework import viewsets
import json,os

class UserViewSet(viewsets.ModelViewSet):
    #fixture_path = os.getcwd()
    #with open(fixture_path + r'/person.json') as f:
     queryset = User.objects.all()
     serializer_class = UserSerializer

class ActivityPeriodViewSet(viewsets.ModelViewSet):
    #fixture_path = os.getcwd()
    #with open(fixture_path + r'/person.json') as f:
     queryset = ActivityPeriod.objects.all()
     serializer_class = ActivityPeriodSerializer
    





