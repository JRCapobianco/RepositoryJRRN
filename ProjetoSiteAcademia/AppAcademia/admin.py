from django.contrib import admin
from .models import Aluno, Funcionario

class AlunosAdmin(admin.ModelAdmin):
    list_display = ('nome', 'plano', 'frequencia')

admin.site.register(Aluno, AlunosAdmin)

class FuncionariosAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cargo')

admin.site.register(Funcionario, FuncionariosAdmin)



