from django.test import TestCase, Client
from django.urls import reverse
from content_app.models import Content, ContentType, FAQ, Category
import json


# todo follow this video to test views: https://www.youtube.com/watch?v=hA_VxnxCHbo

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.home_url = reverse('home')
        self.articles_url = reverse('articles_view')
        self.blog_url = reverse('blog_view')
        self.faq_url = reverse('FAQ')
        self.contact_url = reverse('contact')
        self.podcast_url = reverse('podcast')
        self.test_article = Content.objects.create(
            title='Test Article',
            slug='test-article',
            description='Test Article D escription',
            isPremium=False,
            contentType=ContentType.article
        )
        self.test_blog = Content.objects.create(
            title='Test Blog',
            slug='test-blog',
            description='Test Blog Description',
            isPremium=False,
            contentType=ContentType.blog
        )
        self.test_faq = FAQ.objects.create(
            category=Category.Didactiek,
            question='Test Question',
            answer='Test Answer'
        )

    def test_home_GET(self):
        response = self.client.get(self.home_url)

        self.assertEquals(response.status_code, 200)

    def test_homepage_view_GET(self):
        client = Client()
        response = client.get(reverse('home'))

        self.assertEquals(response.status_code, 200)  # check if the response is 200 means page successfully loaded
        self.assertTemplateUsed(response, 'home.html')  # check if the correct template is used
