from django.test import TestCase

from .models import Talk


class TalkViewTests(TestCase):
    def setUp(self):
        self.talk = Talk.objects.create(name='My preciousssss...', speakers='Gollum')

    def test_index_page_returns_talk(self):
        # The index page of the ratezzz app should exist
        response = self.client.get('/ratezzz/')
        self.assertContains(response, 'My preciousssss...')
