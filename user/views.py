from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request

from user.models import User, UserStage, StandardResultsSetPagination
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
        print(request.data)
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

        if request.data['chat_id']:
            user.chat_id = request.data['chat_id']
            user.save()
        if request.data['type']:
            user.type = request.data['type']
            user.save()
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


class UserPageView(APIView, StandardResultsSetPagination):
    model = User
    serializer = UserSerializer

    def get(self, request: Request):
        results = self.paginate_queryset(self.model.objects.filter(type=request.query_params['user_type']), request, view=self)
        serializer = self.serializer(results, many=True)
        return self.get_paginated_response(serializer.data)

    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'count': self.page.paginator.count,
            'current_page': self.page.number,
            'results': data,
        })

    def delete(self, request: Request, user_id: int):
        try:
            user = self.model.objects.get(id=user_id)
            returnValue = self.serializer(user).data
            user.delete()
            return Response(returnValue, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
