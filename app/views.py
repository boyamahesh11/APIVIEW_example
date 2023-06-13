from django.shortcuts import render
from app.models import *
from app.serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated

# Create your views here.

@api_view()
@permission_classes([IsAuthenticated])
def EmployeeJData(request):
    EQS=Employee.objects.all()
    ESD=EmployeeMS(EQS,many=True)

    return Response(ESD.data)

