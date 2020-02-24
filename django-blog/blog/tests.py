from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from .models import Post


class BlogTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(username='testuser',
                                                         email='test@email.com',
                                                         password='secret')

        self.post = Post.objects.create(title='A good title',
                                        body='Nice body content',
                                        author=self.user)

    def test_string_representation(self):
        post = Post(title='A sample title')
        self.assertEqual(str(post), post.title)

    def test_post_content(self):
        self.assertEqual(f'{self.post.title}', 'A good title')
        self.assertEqual(f'{self.post.author}', 'testuser')
        self.assertEqual(f'{self.post.body}', 'Nice body content')

    def test_post_list_view(self):
        response = self.client.get(reverse('blog:home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Nice body content')
        self.assertTemplateUsed(response, 'blog/home.html')

    def test_post_detail_view(self):
        response = self.client.get('/post/1/')
        no_response = self.client.get('/post/1234567890/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'A good title')
        self.assertTemplateUsed(response, 'blog/post_detail.html')

    def test_create_post_view(self):
        response = self.client.post(reverse('blog:new_post'), {
            'title': 'new title',
            'body': 'new text',
            'author': self.user
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'new title')
        self.assertContains(response, 'new text')

    def test_update_post_view(self):
        response = self.client.post(reverse('blog:edit_post', args='1'), {
            'title': 'updated title',
            'body': 'updated text'
        })
        self.assertEqual(response.status_code, 302)

    def test_delete_post_view(self):
        response = self.client.get(reverse('blog:delete_post', args='1'))
        self.assertEqual(response.status_code, 200)

