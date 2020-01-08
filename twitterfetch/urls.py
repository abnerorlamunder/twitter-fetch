from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.hashtag_list, name='hashtag_list'),
    path('hashtag_delete/<int:pk>', views.HashtagDelete.as_view(), name='hashtag_delete'),
]