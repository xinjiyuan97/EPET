"""
Title: 实验信息序列化
Author: xinjiyuan97
Date: 2018-3-17
"""

from rest_framework import serializers
from experiment.models import Experiments

class ExperimentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source = 'owner.id')
    class Meta:
        model = Experiments
        fields = ('priority', 'Title', 'description', \
            'expermentScore', 'clientView', 'reportTemplete', \
            'owner')