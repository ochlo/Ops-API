# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class CmdProtocols(models.Model):
    CMDPROTOCOLS = (
        ('rest'),
        ('soap'),
        ('telnet'),
        ('tl1'),
        ('ssh'),
    )
    cmdprotocol = models.CharField(max_length=255, choices=CMDPROTOCOLS)
    timestamp = models.DateTimeField(auto_now_add=True)

class CmdSystems(models.Model):
    CMDSYSTEMS = (
        ('ams5520'),
        ('axsvision'),
        ('calix'),
        ('junos'),
        ('junose'),
        ('triad'),
    )
    cmdprotocolkey = models.ForeignKey('CmdProtocols', on_delete=models.CASCADE)
    cmdprotocol = models.CharField(max_length=255, choices=CMDSYSTEMS)
    timestamp = models.DateTimeField(auto_now_add=True)

class CmdSets(models.Model):
    cmdsystemkey = models.ForeignKey('CmdSystems', on_delete=models.CASCADE)
    cmdset = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

class Cmds(models.Model):
    cmdsetkey = models.ForeignKey('CmdSystems', on_delete=models.CASCADE)
    cmdset = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
