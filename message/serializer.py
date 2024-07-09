from rest_framework import serializers

from message.models import Message, DriverOrder
from user.serializers import UserSerializer


class DriverOrderSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = DriverOrder
        fields = '__all__'


class MessageSerializer(serializers.ModelSerializer):
    drivers = DriverOrderSerializer(many=True, read_only=True)

    class Meta:
        model = Message
        fields = '__all__'
