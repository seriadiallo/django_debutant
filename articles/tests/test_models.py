from django.test import TestCase
from django.utils import timezone

from ..models import Article


class ArticleTestCases(TestCase):

    def setUp(self):
        Article.objects.create(titre='Mon titre', description='une description',
         date_pub=timezone.now(), auteur="Mon auteur")
        # self.art2 = Article.objects.create(titre='Mon titre 2', description='une description 2',
        #  date_pub=timezone.now(), auteur="Mon auteur 2")

    def test_str_of_model(self):
        article = Article.objects.get(titre='Mon titre')
        self.assertEquals(article.__str__(), article.titre)

