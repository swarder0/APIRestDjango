from rest_framework import viewsets, generics, filters
from escola.models import Aluno, Curso, Matricula
from escola.serializer import AlunoSerializer, CursoSerializer, MatriculaSerializer, ListaMatriculaAlunoSerializer, ListaMatriculaAlunoCursoSerializer, AlunoSerializerV2
from django_filters.rest_framework import DjangoFilterBackend



class AlunosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os alunos(a)"""

    queryset = Aluno.objects.all()
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nome']
    search_fields = ['nome', 'cpf']
    def get_serializer_class(self):
        if self.request.version =='v2':
            return AlunoSerializerV2
        else:
            return AlunoSerializer
    

class CursosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os cursos"""
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['descricao', 'nivel']
    search_fields = ['codigo_curso', 'descricao']


class MatriculasViewSet(viewsets.ModelViewSet):
    """Exibindo todos os Matriculas"""
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = ['periodo', 'curso']
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]

class ListaMatriculasAlunos(generics.ListAPIView):
    """Listando as Matriculas de um Aluno(a)"""
    def get_queryset(self):
        queryset = Matricula.objects.filter(aluno_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaMatriculaAlunoSerializer

class ListaMatriculasCursos(generics.ListAPIView):
    def get_queryset(self):
        queryset= Matricula.objects.filter(curso_id=self.kwargs['pk'])
        return queryset
    serializer_class =ListaMatriculaAlunoCursoSerializer