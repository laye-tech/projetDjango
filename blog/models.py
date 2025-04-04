from django.db import models

class Article(models.Model):
    titre = models.CharField(max_length=255)
    contenu = models.TextField()
    date_publication = models.DateTimeField(auto_now_add=True)
    auteur = models.CharField(max_length=100)  # Ou ForeignKey vers User
    image = models.ImageField(upload_to="articles/", blank=True, null=True)

    def __str__(self):
        return self.titre
