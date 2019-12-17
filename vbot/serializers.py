
from .models import ViberUser
from rest_framework import serializers



class ViberUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ViberUser
        fields = ['name', 'phone_number']


