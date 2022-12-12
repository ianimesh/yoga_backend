from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponse
from rest_framework import serializers
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
import random
from .models import Subscriber
from .serializers import SubscriberSerializer
from .models import Enrollments
from .serializers import EnrollmentsSerializer
from django.http import JsonResponse


def Index(request):
    return HttpResponse("Hello, world. You're at the index.")

@csrf_exempt
def login(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        try:
            subscriber = Subscriber.objects.get(email=data['email'], password=data['password'])
            return HttpResponse(subscriber.userID, status=200)
        except Subscriber.DoesNotExist:
            return HttpResponse('Invalid username or password', status=401)

def generate_random_id():
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789'
    random_id = ''.join(random.choice(chars) for i in range(8))
    return random_id

@csrf_exempt
def get_random_transaction_id(request):
    if request.method == 'GET':
        random_id = generate_random_id()
        return HttpResponse('{"id":"'+random_id+'"}',status=200)

@csrf_exempt
def add_subscriber(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SubscriberSerializer(data=data)
        if serializer.is_valid():
            try:
                serializer.validate_date_of_birth(data['date_of_birth'])
            except serializers.ValidationError as error:
                return HttpResponse(error, status=400)
            serializer.save()
            return HttpResponse(status=201)
        return HttpResponse(serializer.errors, status=400)

@csrf_exempt
def get_subscriber(request, userID):
    try:
        subscriber = Subscriber.objects.get(userID=userID)
    except Subscriber.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        data = {
            'email': subscriber.email,
            'userID': subscriber.userID,
            'name': subscriber.name,
            'phone_number': subscriber.phone_number,
            'date_of_birth': subscriber.date_of_birth,
            'gender': subscriber.gender
        }
        return JsonResponse(data, status=200)

@csrf_exempt
def get_enrollments(request, userID):
    enrollments = Enrollments.objects.filter(userID=userID)
    serializer = EnrollmentsSerializer(enrollments, many=True)
    return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def create_enrollment(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = EnrollmentsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse(serializer.data, status=201)
        return HttpResponse(serializer.errors, status=400)