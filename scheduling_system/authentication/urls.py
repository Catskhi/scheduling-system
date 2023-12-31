from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from authentication import views

urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('users/create/', views.CreateUser.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)