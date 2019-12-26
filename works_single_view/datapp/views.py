from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from datapp.models import Metadata
from datapp.serializers import MetadataSerializer

# Create your views here.
class MetadataCreateView(ListCreateAPIView):
    queryset = Metadata.objects.all()
    serializer_class = MetadataSerializer

class MetadataDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Metadata.objects.all()
    serializer_class = MetadataSerializer