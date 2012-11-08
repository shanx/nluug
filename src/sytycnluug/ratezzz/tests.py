from django.test import TestCase


class TalkViewTests(TestCase):
    def test_index_page_returns_talk(self):
        # The index page of the ratezzz app should exist
        response = self.client.get('/ratezzz/')
        self.assertEqual(response.status_code, 200)
