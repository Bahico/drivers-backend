from rest_framework import serializers

from user.models import User, UserStage


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class StageSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserStage
        fields = '__all__'
