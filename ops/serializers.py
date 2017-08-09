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
        fields = ('id', 'cmdprotocol', 'cmdsystem', 'cmdset', 'cmdline', 'timestamp')

"""
class CmdSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    cmdprotocol = serializers.ChoiceField(choices=CMDPROTOCOL_CHOICES, default=0)
    cmdsystem = serializers.ChoiceField(choices=CMDSYSTEM_CHOICES, default=0)
    cmdset = serializers.CharField(max_length=255, default='')
    cmdline = serializers.CharField(max_length=255, default='\n')
    timestamp = serializers.DateTimeField(read_only=True, default='')

    def create(self, validated_date):
        return ops.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.cmdprotocol = validated_data.get('cmdprotocol', instance.cmdprotocol)
        instance.cmdsystem = validated_data.get('cmdsystem', instance.cmdsystem)
        instance.cmdset = validated_data.get('cmdset', instance.cmdset)
        instance.cmdline = validated_data.get('cmdline', instance.cmdline)
        instance.save()
        return instance
"""
