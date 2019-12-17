from django.urls import path, include
from .views import ViberUserView, callback, set_webhook, unset_webhook, send_message_for_user, ViberUserListView, ViberUserCreate
from django.contrib import admin


urlpatterns = [
    path('callback/', callback),
    path('set_webhook/', set_webhook),
    path('unset_webhook/', unset_webhook),
    path('send_message/', send_message_for_user),
    path('hi/', ViberUserView.as_view()),
    path('all/', ViberUserListView.as_view(), name='users-all'),
    path('user/add/', ViberUserCreate.as_view())
]
