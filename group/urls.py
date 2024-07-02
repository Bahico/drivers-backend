from django.urls import path
from . import views

urlpatterns = [
    path('filter/<int:group_type>/', views.GroupView.as_view()),
    path('list/', views.GroupListView.as_view()),
    path('create/', views.GroupView.as_view()),
    path('<str:telegram_id>/', views.GroupView.as_view()),
]