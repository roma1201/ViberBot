from viberbot.api.viber_requests import *
from viberbot import Api
from viberbot.api.bot_configuration import BotConfiguration
from viberbot.api.messages import TextMessage, PictureMessage, KeyboardMessage, ContactMessage
from .models import ViberUser
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.views import View
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse
from .utils import viber, registration
from .serializers import ViberUserSerializer
from rest_framework import viewsets

class ViberUserViewSet(viewsets.ModelViewSet):
    queryset=ViberUser.objects.filter(is_active=True)
    serializer_class=ViberUserSerializer


class ViberUserCreate(CreateView):
    model = ViberUser
    fields = ['name', 'language']

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('users_all')


class ViberUserListView(ListView):
    model = ViberUser
    # def get_context_data(self, **kwargs):
    #     context=super().get_context_data(**kwargs)
    #     context['my_var']='test'
    #     return context


class ViberUserView(View):
    def get(self, request):
        return HttpResponse('Hi')

# Create your views here.
bot_configuration = BotConfiguration(
    name='Bot',
    avatar='http://viber.com/avatar.jpg',
    auth_token='4a863d995667d258-a98371a7b3f43af8-c34dcd1049ea7167'
)
viber = Api(bot_configuration)

@csrf_exempt
def set_webhook(request):
  event_types=['failed','delivered','conversation_started']
  url = f'https://{settings.ALLOWED_HOSTS[0]}/viber/callback/'
  viber.set_webhook(url, webhook_events=event_types)
  return HttpResponse('OK')

@csrf_exempt
def unset_webhook(request):
  viber.unset_webhook()  
  return HttpResponse('off')


@csrf_exempt
def callback(request):
    if request.method == 'POST':
        viber_request = viber.parse_request(request.body)
        print(viber_request)
        if isinstance(viber_request, ViberMessageRequest):
            registration(viber_request.sender.id)
            if isinstance(viber_request.message, TextMessage):
                viber.send_messages(viber_request.sender.id, [TextMessage(text ='Hello')])
            elif isinstance(viber_request.message, PictureMessage):
                viber.send_messages(viber_request.sender.id, [TextMessage(text ='img')])
            elif isinstance(viber_request.message, ContactMessage):
                vuser = ViberUser.objects.get(viberid=viber_request.sender.id)
                vuser.phone_number = viber_request.message.contact.phone_number
                vuser.save()
        elif isinstance(viber_request, ViberSubscribedRequest):
                user, created = ViberUser.objects.update_or_create(viberid=viber_request.user.id,
                                               defaults={
                                              'name': viber_request.user.name,
                                              'country': viber_request.user.country,
                                              'language': viber_request.user.language})
                SAMPLE_KEYBOARD = {
                    "Type": "keyboard",
                    "Buttons": [
                        {
                            "Columns": 3,
                            "Rows": 2,
                            "ActionType": "share-phone",
                            "ActionBody": "This will be sent to your bot in a callback",
                            "ReplyType": "message",
                            "Text": "Push me!"
                        }
                    ]
                }
                user = ViberUser.objects.get(id=request.GET.get('user'))
                viber.send_messages(user.viberid,
                                    [KeyboardMessage(tracking_data='tracking_data', keyboard=SAMPLE_KEYBOARD,
                                                                min_api_version=3)])

        elif isinstance(viber_request, ViberUnsubscribedRequest):
                ViberUser.objects.update_or_create(viberid=viber_request.user_id, defaults={'is_active': False})
                print(viber_request)

    return HttpResponse(status=200)


@csrf_exempt
def send_message_for_user(request):
    SAMPLE_KEYBOARD = {
        "Type": "keyboard",
        "Buttons": [
            {
            "Columns": 3,
            "Rows": 2,
            "ActionType": "share-phone",
            "ActionBody": "This will be sent to your bot in a callback",
            "ReplyType": "message",
            "Text": "Push me!"
            }
            ]
        }

    vuser=ViberUser.objects.get(id=request.GET.get('user'))
    viber.send_messages(vuser.viberid, [TextMessage(text=request.GET.get('text')), KeyboardMessage(tracking_data='tracking_data', keyboard=SAMPLE_KEYBOARD, min_api_version=3)])
    return HttpResponse('Hello')


        #viber.send_messages(
            #TextMessage(text='Hi')
            #viber_request.sender.id,
        #)
        

    return HttpResponse(status=200)