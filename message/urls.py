from django.urls import path
from . import views

urlpatterns = [
    path('message/', views.MessageView.as_view()),
    path('message/<int:message_id>/', views.MessageView.as_view()),
    path('order/<int:message_id>/', views.DriverOrderView.as_view()),
    path('cancel-order/', views.OrderCancel.as_view()),
    path('accept-order/', views.OrderAccept.as_view())
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