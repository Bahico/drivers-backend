from django.urls import path
from . import views

urlpatterns = [
    path('', views.UserPageView.as_view()),
    path('delete/<int:user_id>/', views.UserPageView.as_view()),
    path('detail/<int:telegram_id>/', views.UserView.as_view()),
    path('clear-data-base/', views.ClearDataBase.as_view()),
    path('activation/', views.ActivationView.as_view()),
]