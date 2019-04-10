from rest_framework import serializers
from .models import Myapi

class MyapiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Myapi
        fields = ('id','url','name','occupation')
