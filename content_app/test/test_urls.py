
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from content_app.views import homepage_view, articles_view, articles_detail, blog_view


class TestUrls(SimpleTestCase):
    def test_home_page_url_is_resolved(self):
        url = reverse('home')  # find the url that matches the name 'home'
        print(resolve(url))
        self.assertEquals(resolve(url).func, homepage_view)  # check if the url is resolved to the correct url pattern

    def test_articles_view_url_is_resolved(self):
        url = reverse('articles_view')
        print(resolve(url))
        self.assertEquals(resolve(url).func, articles_view)

    def test_articles_detail_url_is_resolved(self):
        url = reverse('article_detail', args=['some-slug'])
        print(resolve(url))
        self.assertEquals(resolve(url).func, articles_detail)

    def test_blog_view_url_is_resolved(self):
        url = reverse('blog_view')
        print(resolve(url))
        self.assertEquals(resolve(url).func, blog_view)