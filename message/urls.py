from django.urls import path
from . import views

urlpatterns = [
    path('message/', views.MessageView.as_view()),
    path('message/<int:message_id>/', views.MessageUpdate.as_view()),
    path('order/<int:message_id>/', views.DriverOrderView.as_view()),
    path('cancel-order/<int:message_id>/', views.OrderCancel.as_view()),
    path('accept-order/<int:message_id>/', views.OrderAccept.as_view()),
    path('send-message/', views.SendMessageView.as_view()),
    path('send-message/<str:message_id>/', views.SendMessageView.as_view()),
]


# {
# "message_id": 12,
# "text": "asfasfas",
# "client": 9,
# "drivers": []
# }
# {
#     "client": 1,
#     "order": 0
# }