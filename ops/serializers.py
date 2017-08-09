from django.contrib.auth.models import User, Group
from rest_framework import serializers
from ops.models import CmdProtocols, CMDPROTOCOLS_CHOICES

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

#class CmdProtocolSerializer(serializers.HyperlinkedModelSerializer):
#    class Meta:
#        model = CmdProtocols
#        fields = ('id', 'cmdprotocol', 'timestamp')

#class CmdProtocolSerializer(serializers.Serializer):
#    id = serializers.IntegerField(read_only=True)
#    cmdprotocol = serializers.ChoiceField(choices=CMDPROTOCOLS_CHOICES, default=0)
#    timestamp = serializers.DateTimeField(read_only=True)

#    def create(self, validated_date):
#        return ops.objects.create(**validated_data)

#    def update(self, instance, validated_data):
#        instance.cmdprotocol = validated_data.get('cmdprotocol', instance.cmdprotocol)
