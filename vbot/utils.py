from .models import ViberUser
from viberbot.api.viber_requests import *
from viberbot import Api
from viberbot.api.bot_configuration import BotConfiguration
from .models import ViberUser

viber = Api(BotConfiguration(
    name='Bot',
    avatar='http://viber.com/avatar.jpg',
    auth_token='4a863d995667d258-a98371a7b3f43af8-c34dcd1049ea7167'))

def registration(v_id):
    v_user, create = ViberUser.objects.update_or_create(viber_id=v_id, defaults={'is_active': True})
    if v_user.phone_number is None:
        SAMPLE_KEYBOARD = {
            "Type": "keyboard",
            "Buttons": [
                {
                "Columns": 6,
                "Rows": 2,
                "BgLoop": True,
                "ActionType": "share-phone",
                "ActionBody": "This will be sent to your bot in a callback",
                "ReplyType": "message",
                "Text": "<font color = "# 7F00FF"> Push me! < font>"
                }
                ]
        }
        text_message = TextMessage(text = 'Nomer Prinyat')
        keyboard_message = KeyboardMessage(tracking_data='tracking_data', keyboard=SAMPLE_KEYBOARD, min_api_version=3)
        viber.send_messages(vuser.viber_id, [text_message, keyboard_message])
