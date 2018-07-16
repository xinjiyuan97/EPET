from rest_framework import serializers
from upload.models import UploadPhotos

class OscilloscopeSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source = 'owner.id')
    class Meta:
        model = UploadPhotos
        fields = ('id', 'filePath', 'owner', 'experimentId', 'resourcesId')
