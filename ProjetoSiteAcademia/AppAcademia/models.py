from django.db import models

#Models Configurados: Aluno & Funcionario // Configured Models: Aluno & Funcionario.

class Aluno(models.Model):
    nome = models.CharField(max_length = 100)
    plano = models.CharField(max_length = 100)
    frequencia = models.CharField(max_length = 100)

    def __str__(self):
        return self.nome
    
class Funcionario(models.Model):
    nome = models.CharField(max_length = 100)
    cargo = models.CharField(max_length = 100)

    def __str__(self):
        return self.nome

