# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

PROTOCOL_CHOICES = (
    (0,''),
    (1,'REST API'),
    (2,'SOAP'),
    (3,'Telnet'),
    (4,'TL1'),
    (5,'SSH'),
)

SYSTEM_CHOICES = (
    (0,''),
    (1,'Nokia AMS5520'),
    (2,'Arris AXSVision'),
    (3,'Calix CMS'),
    (4,'Junos'),
    (5,'Junose'),
    (6,'RedHat'),
    (7,'Tellabs Panorama'),
)

class RedHat(models.Model):
    REDHAT_CHOICES = (
        #(0,''),
        (1,'Red Hat'),
        (2,'CentOS'),
    )
    redhat = models.CharField(max_length=25, choices=REDHAT_CHOICES, default=1)
    protocol = models.CharField(max_length=25, choices=PROTOCOL_CHOICES, default=0)
    timestamp = models.DateTimeField(auto_now_add=True)

class Junos(models.Model):
    PROTOCOL_CHOICES = (
        (0,''),
        (5,'Netconf'),
        (3,'Telnet'),
        (4,'TL1'),
        (5,'SSH'),
    )
    transport = models.CharField(max_length=25, choices=PROTOCOL_CHOICES, default=5)
    port = models.IntegerField(default=22)
    timestamp = models.DateTimeField(auto_now_add=True)

"""
class Cmds(models.Model):
    cmdprotocol = models.CharField(max_length=25, choices=CMDPROTOCOL_CHOICES, default=0)
    cmdsystem = models.CharField(max_length=25, choices=CMDSYSTEM_CHOICES, default=0)
    cmdset = models.CharField(max_length=25, default='')
    cmdline = models.CharField(max_length=255, default='')
    timestamp = models.DateTimeField(auto_now_add=True)
"""
