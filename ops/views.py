# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
#Users, Groups
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from ops.serializers import UserSerializer, GroupSerializer
#Commands
from ops.models import Cmds
from ops.serializers import CmdSerializer
#Depends
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

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

class CmdsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows cmds to be viewed or edited.
    """
    queryset = Cmds.objects.all().order_by('cmdsystem','cmdset')
    serializer_class = CmdSerializer
