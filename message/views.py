from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from message.models import Message, DriverOrder, SendMessage
from message.serializer import DriverOrderSerializer, MessageSerializer, DriverOrderCreateSerializer, \
    SendMessageSerializer, MessageCreateSerializer


# Create your views here.

def model_get(message_id: int) -> Message or bool:
    try:
        return Message.objects.get(message_id=message_id)
    except:
        return False


class MessageView(APIView):
    serializer = MessageSerializer

    def post(self, request: Request):
        serializer = MessageCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        messages = Message.objects.all()
        return Response(self.serializer(messages, many=True).data)


class MessageUpdate(APIView):
    serializer = MessageSerializer
    model = Message

    def get(self, request: Request, message_id: int):
        message = model_get(message_id=message_id)
        if message:
            return Response(self.serializer(message).data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request: Request, message_id: int):
        message = model_get(message_id=message_id)
        if message:
            message.drivers.set(request.data['drivers'])
            message.save()
            return Response(self.serializer(message).data)
        return Response(status=status.HTTP_404_NOT_FOUND)


class OrderCancel(APIView):
    model = Message

    def get(self, request: Request, message_id: int):
        message = model_get(message_id=message_id)
        if message:
            message.driver_order_index = message.driver_order_index + 1
            message.save()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)


class OrderAccept(APIView):
    model = Message

    def get(self, request: Request, message_id: int):
        message = model_get(message_id)
        if message:
            message.accept_driver = \
            DriverOrder.objects.filter(id=message.drivers.values()[message.driver_order_index]['id'])[0]
            message.save()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)


class DriverOrderView(APIView):
    serializer = DriverOrderCreateSerializer
    model = DriverOrder

    def post(self, request: Request, message_id: int):
        message = model_get(message_id)
        if message:
            print(request.data)
            serializer = self.serializer(data={"user": request.data["user"], "order": len(message.drivers.values())})
            if serializer.is_valid():
                serializer.save()
                message.drivers.add(self.model.objects.get(id=serializer.data['id']))
                message.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_404_NOT_FOUND)


class SendMessageView(APIView):
    serializer = SendMessageSerializer
    model = SendMessage

    def post(self, request: Request):
        serializer = self.serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request: Request, message_id: str = None):
        if message_id:
            return Response(self.serializer(self.model.objects.filter(client_message_id=message_id), many=True).data)
        else:
            return Response(status=status.HTTP_200_OK)
