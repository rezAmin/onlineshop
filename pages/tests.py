from django.test import TestCase
from django.urls import reverse


class TestPages(TestCase):
    def test_home_page_view_by_url(self):
        response = self.client.get('/home/')
        self.assertEqual(response.status_code, 200)

    def test_home_page_view_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_home_page_view_template(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'home.html')

    def test_about_page_view_by_url(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)

    def test_about_page_view_by_name(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)

    def test_about_page_view_template(self):
        response = self.client.get(reverse('about'))
        self.assertTemplateUsed(response, 'pages/about.html')

