# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from ops.serializers import UserSerializer, GroupSerializer

from ops.models import Cmds
from ops.serializers import CmdSerializer

#from django.http import HttpResponse, JsonResponse
#from django.views.decorators.csrf import csrf_exempt
#from rest_framework.renderers import JSONRenderer
#from rest_framework.parsers import JSONParser

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
    queryset = Cmds.objects.all()
    serializer_class = CmdSerializer

@api_view(['GET', 'POST'])
def cmds_list(request, format=None):
#    List all, or create a new.
    if request.method == 'GET':
        cmds = Cmds.objects.all()
        serializer = CmdSerializer(cmds, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CmdSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def cmds_detail(request, pk, format=None):
    #Retrieve, update or delete a cmds instance.
    try:
        cmds = cmds.objects.get(pk=pk)
    except cmds.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CmdSerializer(cmds)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CmdSerializer(cmds, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        cmds.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

"""
@csrf_exempt
def cmds_list(request):
#    List all or create a new.
    if request.method == 'GET':
        CmdS = Cmds.objects.all()
        serializer = Cmdserializer(CmdS, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = Cmdserializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def cmds_detail(request, pk):
#    Retrieve, update or delete.
    try:
        cmds = Cmds.objects.get(pk=pk)
    except cmds.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = Cmdserializer(cmds)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = Cmdserializer(cmds, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        cmds.delete()
        return HttpResponse(status=204)
"""
