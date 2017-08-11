# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
#Users, Groups
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from ops.serializers import UserSerializer, GroupSerializer
#Commands
from ops.models import RedHat, Junos, Junose
from ops.serializers import RedHatSerializer, JunosSerializer, JunoseSerializer
#Depends
#from rest_framework import status
#from rest_framework.decorators import api_view
#from rest_framework.response import Response

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class RedHatViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows cmds to be viewed or edited.
    """
    queryset = RedHat.objects.all().order_by('hostname','ip','protocol')
    serializer_class = RedHatSerializer

class JunosViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows cmds to be viewed or edited.
    """
    queryset = Junos.objects.all().order_by('hostname','ip','protocol')
    serializer_class = JunosSerializer
	
class JunoseViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows cmds to be viewed or edited.
    """
    queryset = Junose.objects.all().order_by('hostname','ip','protocol')
    serializer_class = JunoseSerializer
    #lookup_field = 'ip'

