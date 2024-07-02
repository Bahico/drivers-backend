from django.urls import path
from . import views

urlpatterns = [
    path('stage/<int:telegram_id>/', views.UserStageView.as_view()),
    path('<int:telegram_id>/', views.UserView.as_view()),
]