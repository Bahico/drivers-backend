from rest_framework import serializers

from message.models import Message, DriverOrder, SendMessage
from user.serializers import UserSerializer


class DriverOrderSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = DriverOrder
        fields = '__all__'


class DriverOrderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriverOrder
        fields = '__all__'


class MessageSerializer(serializers.ModelSerializer):
    drivers = DriverOrderSerializer(many=True, read_only=True)
    accept_driver = DriverOrderSerializer(read_only=True)
    client = UserSerializer(read_only=True)

    class Meta:
        model = Message
        fields = '__all__'


class MessageCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'


class SendMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SendMessage
        fields = '__all__'
