from django.contrib import admin
from escola.models import Aluno, Curso, Matricula

class Alunos(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email', 'rg', 'cpf', 'data_nascimento')
    list_display_links = ('id', 'nome')
    search_fields = ('nome', 'cpf',)
    list_per_page = 20
    ordering = ('nome',)

admin.site.register(Aluno, Alunos)


class Cursos(admin.ModelAdmin):
    list_display= ('id', 'codigo_curso', 'descricao')
    list_display_links = ('id', 'codigo_curso')
    search_fields = ('codigo_curso',)
    ordering = ('descricao',)

admin.site.register(Curso, Cursos)

class Matriculas(admin.ModelAdmin):
    list_display= ('id', 'aluno', 'curso')
    list_display_links = ('id',)
    

admin.site.register(Matricula, Matriculas)