"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from articles.models import Article

class ArticleTest(TestCase):
    def test_create_article(self):
        """
        Tests that an article can be created
        """
        article = Article(name='name',header='header')
        article.save()

        self.assertEqual(article.creation_date.date(), article.last_updated_date.date())

