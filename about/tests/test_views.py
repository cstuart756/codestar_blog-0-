from django.test import TestCase
from django.urls import reverse


class TestAboutView(TestCase):
    def test_render_about_page(self):
        """
        Simple GET test: about page loads.
        """
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Let&#x27;s Collaborate!", response.content)

    def test_successful_collaboration_request_submission(self):
        """Test for a user requesting a collaboration"""
        post_data = {
            "name": "test name",
            "email": "test@email.com",
            "message": "test message",
        }

        response = self.client.post(reverse("about"), post_data)

        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b"Collaboration request received! I endeavour to respond within 2 working days.",
            response.content,
        )
