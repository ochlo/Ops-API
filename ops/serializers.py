from django.contrib.auth.models import User, Group
from rest_framework import serializers
from ops.models import RedHat, Junos, Junose
#Cmds, CMDPROTOCOL_CHOICES, CMDSYSTEM_CHOICES

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class RedHatSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RedHat
        fields = ('url', 'hostname', 'ip', 'protocol', 'timestamp')

class JunosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Junos
        fields = ('url', 'hostname', 'ip', 'protocol', 'timestamp')
		
class JunoseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Junose
        fields = ('url', 'hostname', 'ip', 'protocol', 'timestamp')

#fields = ('url', 'cmdprotocol', 'cmdsystem', 'cmdset', 'cmdline', 'timestamp', 'port', 'protocol', 
