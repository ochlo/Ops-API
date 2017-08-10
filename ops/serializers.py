from django.contrib.auth.models import User, Group
from rest_framework import serializers
from ops.models import Cmds, CMDPROTOCOL_CHOICES, CMDSYSTEM_CHOICES

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class CmdSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cmds
        fields = ('url', 'cmdprotocol', 'cmdsystem', 'cmdset', 'cmdline', 'timestamp')
