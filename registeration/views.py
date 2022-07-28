from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import status
from .models import *
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def onboard_user(request):
    data = request.POST
    print(data)
    name = data.get('name')
    email = data.get('email')
    if not name or not email:
        return JsonResponse({'msg': 'Please provide name and email'}, status = status.HTTP_400_BAD_REQUEST)
    try:
        print(User.objects.create(name = name, email = email))
        id ='wait'
        return JsonResponse({'id': id}, status = status.HTTP_201_CREATED)
    except Exception as ex:
        print(ex)
        return JsonResponse({'msg': 'Work In Progress'}, status = status.HTTP_400_BAD_REQUEST)
    
def get_newsletter(request):
    data = request.POST
    try:
        User.objects.create(*data)
        return JsonResponse({'msg': 'Work In Progress'}, status = status.HTTP_201_CREATED)
    except Exception as ex:
        print(ex)
        return JsonResponse({'msg': 'Work In Progress'}, status = status.HTTP_400_BAD_REQUEST)

def subscribe_newsletter(request):
    data = request.data
    try:
        User.objects.create(*data)
        return JsonResponse({'msg': 'Work In Progress'}, status = status.HTTP_201_CREATED)
    except Exception as ex:
        print(ex)
        return JsonResponse({'msg': 'Work In Progress'}, status = status.HTTP_400_BAD_REQUEST)
