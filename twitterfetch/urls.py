from django.urls import path
from . import views

urlpatterns = [
    path('', views.hashtag_list, name='hashtag_list'),
]