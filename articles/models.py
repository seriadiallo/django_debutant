from django.db import models

# Create your models here.

class Article(models.Model):


    titre = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    date_pub = models.DateTimeField(null=True)
    auteur = models.CharField(max_length=100)

    def __str__(self):
        return self.titre
    


class Commentaire(models.Model):

    contenu = models.TextField(null=False)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)