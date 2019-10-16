from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse

from django.contrib.auth.models import User
from map.models import Report
from map.api.serializer import ReportSerializer, DataSerailizer


@api_view(['POST',])
@permission_classes((IsAuthenticated,))
def api_create_report(request):

    account = request.user

    report = Report(user = account)

    if request.method == 'POST':
        serializer = ReportSerializer(report, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET',])
def api_get_data(request):
    account = request.user
    
    data = list((Report.objects.filter(user = account)).values())

    return JsonResponse(data, safe = False)