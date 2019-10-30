from rest_framework import serializers

from map.models import Report

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ['lat', 'lon', 'intensity_x', 'intensity_y', 'intensity_z', 'intensity_module', 'vehicle_type'] # da metterci gli altri campi ancora: DONE

class DataSerailizer(serializers.ModelSerializer):
    class Meta: 
        model = Report
        fields = ['user', 'time' ]