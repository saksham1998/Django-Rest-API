
from django.shortcuts import render
from rest_framework import viewsets
from .models import Myapi
from .serializers import MyapiSerializer

class MyapiView(viewsets.ModelViewSet):
    queryset = Myapi.objects.all()
    serializer_class = MyapiSerializer
