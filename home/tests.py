from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Post

class BlogPosts(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username = "johndoe",
            email = "john@doe.com",
            password = "qwer123#"
        )
        self.post = Post.objects.create(
            title = "Test Post",
            author = self.user,
            body = "Lorem ipsum dolor sit amet consectetur..."
        )

    def test_string_representation(self):
        post = Post(title = "Django Test", author=self.user)
        self.assertEqual(str(post), f"{post.title} / {post.author}")
    
    def test_post_content(self):
        self.assertEqual(f"{self.post.title}", "Test Post")
        self.assertEqual(f"{self.post.author}", "johndoe")
        self.assertEqual(f"{self.post.body}", "Lorem ipsum dolor sit amet consectetur...")
    
    def test_post_noresponse(self):
        no_response = self.client.get('post/999')
        self.assertEqual(no_response.status_code, 404)