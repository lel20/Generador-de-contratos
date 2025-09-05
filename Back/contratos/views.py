from django.shortcuts import render
from .models import plantillaContrato
from .serializers import plantillaContratoSerilizer
from rest_framework import generics

class principal(generics.ListCreateAPIView):
    queryset=plantillaContrato.objects.all()
    serializer_class=plantillaContratoSerilizer

