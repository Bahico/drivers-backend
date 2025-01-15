from rest_framework import serializers

from user.models import User, ActivationKey


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class ActivationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivationKey
        fields = '__all__'
