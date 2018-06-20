
from rest_framework import serializers
from lessons.models import LabServers, StudentRequests

class LabServerSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source = 'owner.id')
    
    class Meta:
        model = LabServers
        fields = ('id', 'labNum', 'labStatus', 'owner')

class StudentRequestSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source = 'owner.id')

    class Meta:
        model = StudentRequests
        fields = ('id', 'labNum', 'tableNum', 'date', 'experimentId', 'resourcesId', 'requestClasses', 'reponseContent', 'reponseClasses', 'requestStatus', 'owner')