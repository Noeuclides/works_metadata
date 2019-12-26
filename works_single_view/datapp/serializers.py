from rest_framework.serializers import ModelSerializer

from datapp.models import Metadata

class MetadataSerializer(ModelSerializer):
    class Meta:
        model = Metadata
        fields = ('title', 'contributors', 'iswc')