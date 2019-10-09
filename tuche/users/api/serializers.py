from rest_framework import serializers

#from map.models import Report
from django.contrib.auth.models import User


class RegistrationSerializer(serializers.ModelSerializer):
    
    #password2 = serializer.CharField(style={'input_type':'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password'] #TODO da metterci gli altri campi ancora