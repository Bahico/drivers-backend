from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from group.models import Group
from group.serializers import GroupSerializer


# Create your views here.


class GroupView(APIView):
    @staticmethod
    def get_object(telegram_id):
        try:
            return Group.objects.get(id=telegram_id)
        except:
            return False

    @staticmethod
    def get(request: Request, group_type: int):
        groups = Group.objects.filter(type=group_type)
        return Response(GroupSerializer(groups, many=True).data)

    @staticmethod
    def post(request: Request):
        serializer = GroupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request, telegram_id: str):
        print(telegram_id, type(telegram_id))
        group = self.get_object(telegram_id)
        print(group, telegram_id)
        if group:
            group.delete()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)


class GroupListView(APIView):
    def get(self, request: Request):
        groups = Group.objects.all()
        return Response(GroupSerializer(groups, many=True).data)
