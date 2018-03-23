"""
Title: 实验信息显示
Author: xinjiyuan97
Date: 2018-3-17
"""

from django.shortcuts import render
from experiment.models import Experiments
from rest_framework import generics
from rest_framework import permissions
from experiment.serializers import ExperimentSerializer
from rest_framework.views import APIView
from utils.permissions import IsOwnerOrReadOnly, IsTeacher
from users.models import UserInfo

# Create your views here.
def getAllExperiments():
    experiments = Experiments.objects.all()
    return experiments

def getExperiment(title):
    try:
        experiment = Experiments.objects.filter(belongs = title)
    except Users.DoesNotExist as e:
        return None
    return experiment

class ShowAllExperiments(generics.ListAPIView):
    queryset = getAllExperiments()
    serializer_class = ExperimentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
    

class ShowExperiment(APIView):
    def get(self, request, format = None):
        title = request.GET['title']
        experiment = getExperiment(title)
        serializer = ExperimentSerializer(experiment.data, many = True)
        return Response(serializer.data)

class AddExperiment(generics.CreateAPIView):
    queryset = getAllExperiments()
    serializer_class = ExperimentSerializer
    
    permission_classes = (permissions.IsAuthenticated, IsTeacher)
    def perform_create(self, serializer):
        serializer.save(owner = UserInfo.objects.get(userAccount = self.request.user))
    # 