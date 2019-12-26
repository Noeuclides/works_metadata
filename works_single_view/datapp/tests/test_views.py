from django.shortcuts import reverse

from rest_framework.test import APITestCase

from datapp.models import Metadata


class TestNoteApi(APITestCase):
    def setUp(self):
        # create metadata
        self.met = Metadata(title="psyco", contributors="SOAD", iswc="T91294141")
        self.met.save()

    def test_metadata_creation(self):
        response = self.client.post(reverse('metadata'), {
            'title': 'one',
            'contributors': 'Metallica',
            'iswc': 'T283841341'
        })

        # assert new metadata was added
        self.assertEqual(Metadata.objects.count(), 2)

        # assert a created status code was returned
        self.assertEqual(201, response.status_code)

    def test_getting_metadata(self):
        response = self.client.get(reverse('metadata'), format="json")
        self.assertEqual(len(response.data), 1)

    def test_updating_metadata(self):
        print(reverse('detail', kwargs={'tittle', 'one'}))
        response = self.client.put(reverse('detail', kwargs={'title': 'one'}), {
            'title': 'one',
            'contributors': 'U2',
            'iswc': 'T81284191'
        }, format="json")

        # check info returned has the update
        self.assertEqual('one', response.data['title'])

    def test_deleting_metadata(self):
        response = self.client.delete(reverse('detail', kwargs={'title': 'one'}))

        self.assertEqual(204, response.status_code)