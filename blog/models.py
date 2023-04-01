from django.db import models
from django.shortcuts import reverse


class Post(models.Model):
    STATUS_CHOICES = (
        ('pub', 'published'),
        ('drf', 'draft'),
    )
    title = models.CharField(max_length=50)
    text = models.TextField()
    author = models.ForeignKey(to='auth.User', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=STATUS_CHOICES, max_length=3)

    def get_absolut_url(self):
        return reverse('posts_detail', args=[self.id])

    def __str__(self):
        return self.title
