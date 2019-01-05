# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse,HttpResponse
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from wishes.models import Wish
from wishes.serializers import WishSerializer
from rest_framework import generics

class WishList(generics.ListCreateAPIView):
    queryset = Wish.objects.all()
    serializer_class = WishSerializer

class WishDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Wish.objects.all()
    serializer_class = WishSerializer