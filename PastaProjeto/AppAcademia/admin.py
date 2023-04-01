from django.contrib import admin
from .models import Aluno, Funcionario

class AlunosAdmin(admin.ModelAdmin):
    list_display = ('Nome', 'Plano', 'Telefone', 'RG')

admin.site.register(Aluno, AlunosAdmin)

class FuncionariosAdmin(admin.ModelAdmin):
    list_display = ('Nome', 'Cargo', 'Telefone', 'RG')

admin.site.register(Funcionario, FuncionariosAdmin)




