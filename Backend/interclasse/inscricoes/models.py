from django.db import models

# Create your models here.

class Equipes(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
    
class Inscricao(models.Model):
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)

    MODALIDADES = [
        ("FUTSAL", "Futsal"),
        ("VOLEI", "Vôlei"),
        ("TENIS-DE-MESA", "Tênis-de-mesa"),
    ] 
    modalidade = models.CharField(
        max_length=20,
        choices=MODALIDADES
    )