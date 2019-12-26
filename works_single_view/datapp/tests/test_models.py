from django.test import TestCase

from datapp.models import Metadata


class TestMetadataModel(TestCase):
    def setUp(self):
        self.met = Metadata(title="Songto", contributors="blur", iswc="T9293010")
        self.met.save()

    def test_metadata_creation(self):
        self.assertEqual(Metadata.objects.count(), 1)

    def test_metadata_representation(self):
        self.assertEqual(self.met.title, str(self.met))