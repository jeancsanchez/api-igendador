from django.shortcuts import render

# Create your views here.
from rest_framework.schemas import views

from establishment.models import Photo, Establishment


class View(views.APIView):
    Establishment.objects
