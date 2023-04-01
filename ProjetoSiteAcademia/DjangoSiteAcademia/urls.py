
from django.contrib import admin
from django.urls import path, include
from AppAcademia.views import AlunoViewset, FuncionarioViewset
from rest_framework import routers

#Routers configurados: 'Alunos' & 'Funcionarios' // Configured Routers: 'Alunos' e 'Funcionarios'

router = routers.DefaultRouter()
router.register('Alunos', AlunoViewset, basename='Alunos')
router.register('Funcionarios', FuncionarioViewset, basename='Funcionarios')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
