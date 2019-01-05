# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse,HttpResponse
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from wishes.models import Wish
from wishes.serializers import WishSerializer

@csrf_exempt
def wish_list(request):
    """
    List all wishes or create a new wish
    """
    if request.method == 'GET':
        wishes = Wish.objects.all()
        serializer = WishSerializer(wishes, many=True)
        return JsonResponse(serializer.data, safe=False)

    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = WishSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def wish_detail(request,pk):
    """
    Retrieve, update or delete a birthday wish.
    """
    try:
        wish = Wish.objects.get(pk=pk)
    except Wish.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = WishSerializer(wish)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = WishSerializer(wish, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        wish.delete()
        return HttpResponse(status=204)
