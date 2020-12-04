from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from django.template import loader
from django.contrib import auth
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
import json

from .models import UserRegistrar
from .serializers import RegisterSerializer, LoginSerializer


def home_view(request):
    return render(request, "base.html")


@method_decorator(csrf_exempt)
def register_form(request):
    return render(request, "registration.html")


def login_form(request):
    return render(request, "login.html")


@method_decorator(csrf_exempt)
def registered_form(request):
    if request.method == "POST":
        fname = request.POST.get("registrar_fname")
        lname = request.POST.get("registrar_lname")
        username = request.POST.get("registrar_username")
        email = request.POST.get("registrar_email")
        phone = request.POST.get("registrar_phone")
        password = request.POST.get("password")
        registrar_type = ""
        V = request.POST.get("button_2")
        if V is not None:
            registrar_type = "V"
        else:
            registrar_type = "B"

        x = {
            "registrar_fname": fname,
            "registrar_lname": lname,
            "registrar_username": username,
            "registrar_email": email,
            "registrar_phone": phone,
            "password": password,
            "registrar_type": registrar_type,
        }

        ser = RegisterSerializer(data=x)
        print(ser.initial_data)
        if ser.is_valid():
            ser.save()
            return HttpResponse(
                "User registered successfully:)", status=status.HTTP_201_CREATED
            )
        return HttpResponse(ser.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "GET":
        return render(request, "registered.html")


@method_decorator(csrf_exempt)
def registration_bidder_view(request):

    if request.method == "POST":
        print(request.POST)
        serializer = RegisterSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save(serializer)
            return HttpResponse(
                "Bidder registered successfully:)", status=status.HTTP_201_CREATED
            )
        return HttpResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@method_decorator(csrf_exempt)
def registration_vendor_view(request):

    if request.method == "POST":
        print(request.POST)
        serializer = RegisterSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save(serializer)
            return HttpResponse(
                "Vendor registered successfully:)", status=status.HTTP_201_CREATED
            )
        return HttpResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@method_decorator(csrf_exempt)
def registration_view(request, registrar_type):

    if request.method == "GET":
        print("ABC")
        print(request.GET)
        serializer = RegisterSerializer(data=request.GET)
        print(serializer.initial_data)
        if serializer.is_valid():
            serializer.save(serializer)
            return HttpResponse(
                "Vendor registered successfully:)", status=status.HTTP_201_CREATED
            )
        return HttpResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def login_request(request):
    if request.method == "POST":
        username = request.POST.get("registrar_username")
        password = request.POST.get("password")
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponse(user, status=status.HTTP_202_ACCEPTED)
        return HttpResponse(
            "Unauthorized user.. OOPS! SORRY", status=status.HTTP_401_UNAUTHORIZED
        )