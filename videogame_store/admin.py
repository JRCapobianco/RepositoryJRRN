from django.contrib import admin
from .models import Jogo,Loja

class JogosAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco')


admin.site.register(Jogo, JogosAdmin)


class LojaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'endereco', 'telefone')


admin.site.register(Loja, LojaAdmin)



