
from django.contrib import admin
from django.urls import path

from . import views

app_name = 'meeting'

urlpatterns = [
    path('', views.home, name='home'),
    path('meeting/<uuid:meeting_id>/', views.meeting, name='meeting'),
    path('join-meeting/<uuid:meeting_id>/', views.join_meeting, name='join-meeting'),
]
