from django.db import models

# Models Configurados: Aluno & Funcionario // Configured Models: Aluno & Funcionario.

class Aluno(models.Model):
    Nome = models.CharField(max_length = 100, blank = False)
    Plano = models.CharField(max_length = 100, blank = False)
    Telefone = models.CharField(max_length = 20, blank = True) 
    RG = models.CharField(max_length = 10, blank = False) 
    #Preencher todos os campos será obrigatório.


    def __str__(self):
        return self.Nome
    
class Funcionario(models.Model):
    Nome = models.CharField(max_length = 100, blank = False)
    Cargo = models.CharField(max_length = 100, blank = False)
    Telefone = models.CharField(max_length = 20, blank = True) 
    RG = models.CharField(max_length = 10, blank = True)
    #Preencher todos os campos será obrigatório.


    def __str__(self):
        return self.Nome
    


