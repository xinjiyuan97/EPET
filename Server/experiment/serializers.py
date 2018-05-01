"""
Title: 实验信息序列化
Author: xinjiyuan97
Date: 2018-3-17
"""

from rest_framework import serializers
from experiment.models import Experiments, ContentOfClass, JudgeRequest, ExperimentScore

class ExperimentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source = 'owner.id')
    class Meta:
        model = Experiments
        fields = ('id', 'priority', 'Title', 'description', \
            'expermentScore', 'clientView', 'reportTemplete', \
            'owner')

class ExperimentTitleSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source = 'owner.id')
    class Meta:
        model = Experiments
        fields = ('id', 'priority', 'Title', 'expermentScore', 'owner')

class LessonsSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source = 'owner.id')
    class Meta:
        model = ContentOfClass
        fields = ('id', 'Title', 'experments', 'owner')

class JudgeRequestSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source = 'owner.id')
    class Meta:
        model = JudgeRequest
        fields = ('id', 'Title', 'report', 'requestStatus', 'Status', 'owner')

class ScoreSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source = 'owner.id')
    class Meta:
        model = ExperimentScore
        fields = ('id', 'Title', 'date', 'owner')