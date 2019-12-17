from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from vbot import views
from vbot.views import set_webhook, unset_webhook
from django.urls import include, path
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'Viberusers', views.ViberUserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('viber/', include('vbot.urls')),
    path('user/', include('user.urls')),
    path('events/', include('events.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('vbot/', include('vbot.urls')),


]
