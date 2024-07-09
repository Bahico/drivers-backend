from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from message.models import Message, DriverOrder
from message.serializer import DriverOrderSerializer, MessageSerializer


# Create your views here.

def model_get(message_id: int) -> Message or bool:
    try:
        return Message.objects.get(message_id=message_id)
    except:
        return False


class MessageView(APIView):
    serializer = MessageSerializer
    model = Message

    def post(self, request: Request):
        serializer = self.serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request: Request, message_id: int):
        message = model_get(message_id=message_id)
        if message:
            return Response(self.serializer(message, partial=True).data)
        return Response(status=status.HTTP_404_NOT_FOUND)


class OrderCancel(APIView):
    model = Message

    def get(self, request: Request, message_id: int):
        message = model_get(message_id=message_id)
        if message:
            print(message.driver_order_index)
            if len(message.drivers) > message.driver_order_index:
                message.update(driver_order_index=message.driver_order_index + 1)
                message.save()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)


class OrderAccept(APIView):
    model = Message

    def get(self, request: Request, message_id: int):
        message = model_get(message_id)
        if message:
            message.update(accept_driver=message.drivers[message.driver_order_index])
            message.save()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)


class DriverOrderView(APIView):
    serializer = DriverOrderSerializer
    model = DriverOrder

    def post(self, request: Request, message_id: int):
        message = model_get(message_id)
        if message:
            serializer = self.serializer(data={"user": request.data["user"], "order": len(message.drivers.values())})
            if serializer.is_valid():
                serializer.save()
                message.drivers.add(self.model.objects.get(id=serializer.data['id']))
                message.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_404_NOT_FOUND)
