from django.test import Client, TestCase
from django.urls import resolve, reverse
from django.utils import timezone


from articles.models import Article


class TestView(TestCase):

    def setUp(self):
        self.client = Client()
        self.article = Article.objects.create(
            titre='Mon premier titre',
            description='Ceci est une description de mon article',
            date_pub=timezone.now(),
            auteur='Mon premier auteur'
        )

    def test_article_index_GET(self):

        response = self.client.get(reverse('articles:index'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'articles/index.html')
    
    def test_home_GET(self):
        response = self.client.get(reverse('home'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'articles/home.html')

    def test_article_create_GET(self):
        response = self.client.get(reverse('articles:create'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'articles/create.html')
    

    def test_article_create_POST(self):
        response = self.client.post(reverse('articles:create'),{
            'titre': 'Mon titre',
            'description': "Ma description pour ce post",
            'date_pub': timezone.now(),
            'auteur': "Mon auteur"
        })
        self.assertEquals(response.status_code, 301)

    
    def test_article_create_empty_value_POST(self):
        response = self.client.post(reverse('articles:create'),{})
        self.assertEquals(response.status_code, 200)


    def test_article_malist_GET(self):
        response = self.client.get(reverse('articles:list'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'articles/list.html')


class ArticleDeleteTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.article = Article.objects.create(
            titre='Article a supprimer',
            description="la description de cet article qui va etre .....",
            date_pub=timezone.now(),
            auteur='Un mauvais auteur'
        )
        self.delet_url = reverse('articles:delete', kwargs={'id': self.article.id})
    
    def test_used_template(self):
        response = self.client.get(self.delet_url)
        self.assertTemplateUsed(response, template_name='articles/article_delete_confirm.html')
    
    def test_contains_csrf(self):
        response = self.client.get(self.delet_url)
        self.assertContains(response, 'csrfmiddlewaretoken')
    
    def test_article_delete_POST(self):
        response = self.client.post(self.delet_url, {})
        self.assertEquals(response.status_code, 302)
    
    def test_article_delete_not_found(self):
        url = reverse('articles:delete', kwargs={'id': 456})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)