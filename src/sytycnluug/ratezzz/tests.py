from django.test import TestCase

from .models import Talk


class TalkViewTests(TestCase):
    def setUp(self):
        self.talk = Talk.objects.create(name='My preciousssss...', speakers='Gollum')

    def test_index_page_returns_talk(self):
        # The index page of the ratezzz app should exist
        response = self.client.get('/ratezzz/')
        self.assertContains(response, 'My preciousssss...')

    def test_rate_talk(self):
        # Talk doesn't have a rating
        self.assertFalse(self.talk.rating_set.exists())

        # Sending post request to talk at ratezzz/1/ creates a rating for this talk
        self.client.post('/ratezzz/1/', data={'rating': 5})
        rating = self.talk.rating_set.get()
        self.assertEqual(rating.rating, 5)
