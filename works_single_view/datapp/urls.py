from django.conf.urls import url

from datapp.views import MetadataCreateView, MetadataDetailView

urlpatterns = [
    url(r'^metadata/$', MetadataCreateView.as_view(), name='metadata'),
    url(r'^metadata/(?P<stub>[-\W]+)$', MetadataDetailView.as_view(), name='detail'),
]