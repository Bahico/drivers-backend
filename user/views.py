from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request

from user.models import User, UserStage
from user.serializers import UserSerializer, StageSerializer


# Create your views here.

class UserView(APIView):

    def get(self, request: Request, telegram_id: int = None):
        if telegram_id:
            country = self.get_object(telegram_id)
            serializer = UserSerializer(country)
            return Response(serializer.data)
        else:
            countries = User.objects.all()
            serializer = UserSerializer(countries, many=True)
            return Response(serializer.data)

    def post(self, request: Request, telegram_id: int):
        user = self.get_object(telegram_id)
        if not user:
            if not request.data['type']:
                request.data['type'] = 3
            serializer = UserSerializer(data=request.data)

            stage_serializer = StageSerializer(data={
                "telegram_id": telegram_id,
                "step": "start"
            })

            if serializer.is_valid():
                serializer.save()
                if stage_serializer.is_valid():
                    stage_serializer.save()
                print(stage_serializer.errors, ': stage')
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            print(serializer.errors, ': user')
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request: Request, telegram_id: int):
        region = self.get_object(telegram_id)
        serializer = UserSerializer(region, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def get_object(telegram_id):
        try:
            return User.objects.get(telegram_id=telegram_id)
        except:
            return False


class UserStageView(APIView):

    @staticmethod
    def get_object(telegram_id):
        try:
            return UserStage.objects.get(telegram_id=telegram_id)
        except:
            return False

    def get(self, request: Request, telegram_id: int):
        user_stage = self.get_object(telegram_id)
        if user_stage:
            return Response(StageSerializer(user_stage).data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request: Request, telegram_id: int):
        user_stage = self.get_object(telegram_id)
        if user_stage:
            serializer = StageSerializer(user_stage, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_404_NOT_FOUND)
