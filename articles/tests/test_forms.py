from django.test import TestCase
from django.utils import timezone

from articles.forms import ArticleForm


class ArticleFormTest(TestCase):

    def test_article_form_with_valid_data(self):
        form = ArticleForm(data={
            'titre': "Un titre",
            'description': 'Une description',
            'date_pub': timezone.now(),
            'auteur': "Nom de l'auteur"
        })
        self.assertTrue(form.is_valid())
        self.assertEquals(len(form.cleaned_data), 4)
    

    def test_article_form_with_no_data(self):
        form = ArticleForm({})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 4)