from django.test import TestCase
from django.urls import reverse


class HomeViewGetRequestTests(TestCase):
    def test_home_view_url_exists_at_proper_location_and_uses_proper_template_1(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'learnsql/home.html')

    def test_home_view_url_exists_at_proper_location_and_uses_proper_template_2(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'learnsql/home.html')

 # test post requests
