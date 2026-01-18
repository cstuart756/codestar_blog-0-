from django.test import TestCase
from django.urls import reverse

from .models import About
from .forms import CollaborateForm


class TestAboutView(TestCase):

    def setUp(self):
        self.about_content = About.objects.create(
            title="About Me",
            content="This is about me."
        )

    def test_render_about_page_with_collaborate_form(self):
        response = self.client.get(reverse('about'))

        self.assertEqual(response.status_code, 200)
        self.assertIn(b'About Me', response.content)
        self.assertIn(b'This is about me.', response.content)
        self.assertIsInstance(response.context['collaborate_form'], CollaborateForm)
