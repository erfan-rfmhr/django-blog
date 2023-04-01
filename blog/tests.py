from django.contrib.auth.models import User
from django.test import TestCase
from django.shortcuts import reverse, get_object_or_404
from django.http.response import Http404
from .models import Post


# Create your tests here.
class TestBlog(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(username='user1')
        cls.post1 = Post.objects.create(
            title='post1',
            text='text1',
            author=cls.user,
            status=Post.STATUS_CHOICES[0][0]
        )
        cls.post2 = Post.objects.create(
            title='post2',
            text='text2',
            author=cls.user,
            status=Post.STATUS_CHOICES[1][0]
        )

    def test_post_str(self):
        title = self.post1.title
        self.assertEqual(str(self.post1), title)

    def test_post_in_post_lists_view(self):
        response = self.client.get(reverse('posts_list'))
        self.assertContains(response, self.post1.title)
        self.assertNotContains(response, self.post2.title)

    def test_create_post_view(self):
        response = self.client.post(reverse('post_create'), {
            'title': 'new title',
            'text': 'new text',
            'status': 'pub',
            'author': self.user.id,
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.last().title, 'new title')

    def test_update_post_view(self):
        response = self.client.post(reverse('post_update', args=[self.post2.id]), {
            'title': 'updated title',
            'text': 'updated text',
            'author': self.user.id,
            'status': 'pub',
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.last().title, 'updated title')

    def test_delete_post_view(self):
        response = self.client.post(reverse('post_delete', args=[self.post2.id]))
        self.assertEqual(response.status_code, 302)
        self.assertRaises(Http404, lambda: get_object_or_404(Post, pk=self.post2.id))
