from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from blog.models import Post


class TestBlogViews(TestCase):
    def setUp(self):
        """
        Create a user and a published blog post that we can test against.
        """
        User = get_user_model()
        self.user = User.objects.create_superuser(
            username="myUsername",
            email="test@email.com",
            password="myPassword",
        )

        # Create a published post with a known slug.
        # Adjust fields here if your Post model requires different ones.
        self.post = Post.objects.create(
            title="Blog Title",
            slug="blog-title",
            author=self.user,
            content="Test content",
            status=1,  # Common in CI projects: 0=draft, 1=published
            excerpt="Test excerpt",
        )

    def test_render_post_list_page(self):
        """
        Example GET test: post list page loads.
        Adjust URL name if your list view name differs.
        """
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Blog", response.content)

    def test_render_post_detail_page(self):
        """
        Example GET test: post detail page loads for our created post.
        """
        response = self.client.get(reverse("post_detail", args=[self.post.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Blog Title", response.content)

    def test_successful_comment_submission(self):
        """Test for posting a comment on a post"""
        self.client.login(username="myUsername", password="myPassword")

        post_data = {
            "body": "This is a test comment."
        }

        # IMPORTANT FIX: Use the actual slug that exists in setUp() => "blog-title"
        response = self.client.post(
            reverse("post_detail", args=["blog-title"]),
            post_data
        )

        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b"Comment submitted and awaiting approval",
            response.content
        )
