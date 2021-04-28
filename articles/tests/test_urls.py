from django.test import SimpleTestCase
from django.urls import reverse, resolve

from ..views import index, create, detail, home


class TestUrlsResolve(SimpleTestCase):


    def test_index_article_resolve(self):
        url = reverse('articles:index')
        self.assertEquals(resolve(url).func, index)
    
    def test_create_article_resolve(self):
        url = reverse('articles:create')
        self.assertEquals(resolve(url).func, create)

    def test_detail_article_resolve(self):
        url = reverse('articles:detail', args=[1])
        self.assertEquals(resolve(url).func, detail)
    
    def test_home_article_resolve(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func, home)