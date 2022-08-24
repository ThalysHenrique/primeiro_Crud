from django.db import models

class Livro(models.Model):
    nome = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return self.nome
    
