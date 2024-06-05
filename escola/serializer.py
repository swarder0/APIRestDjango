from rest_framework import serializers
from escola.models import Aluno, Curso, Matricula


class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = '__all__'
    def validate_cpf(self, cpf):
        if len(cpf) != 11:
            raise serializers.ValidationError('CPF deve conter 11 dígitos.')
        return cpf
    def validate_nome(self, nome):
        if not nome.isalpha():
            raise serializers.ValidationError('O nome deve conter apenas letras.')
        return nome
    def validate_rg(self, rg):
        if len(rg) != 9:
            raise serializers.ValidationError('RG deve conter 9 dígitos.')
        return rg

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'

class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        exclude = []

class ListaMatriculaAlunoSerializer(serializers.ModelSerializer):
    curso = serializers.ReadOnlyField(source='curso.descricao')
    periodo = serializers.SerializerMethodField()
    class Meta:
        model = Matricula
        fields = ['curso', 'periodo']
    def get_periodo(self, obj):
        return obj.get_periodo_display()

class ListaMatriculaAlunoCursoSerializer(serializers.ModelSerializer):
    aluno_nome = serializers.ReadOnlyField(source='aluno.nome')
    class Meta:
        model =Matricula
        fields = ['aluno_nome']