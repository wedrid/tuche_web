from rest_framework import serializers

from map.models import Report

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ['lat', 'lon'] #TODO da metterci gli altri campi ancora