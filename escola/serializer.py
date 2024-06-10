from rest_framework import serializers
from escola.models import Aluno, Curso, Matricula
from escola.validators import *


class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = '__all__'
    def validate(self, data):
        if not validate_cpf(data['cpf']):
            raise serializers.ValidationError({'cpf':'CPF invalido, por favor digite um CPF valido.'})
        if not validate_nome(data['nome']):
            raise serializers.ValidationError({'nome':'O nome deve conter apenas letras.'})
        if validate_rg(data['rg']):
            raise serializers.ValidationError({'rg':'RG deve conter 9 dígitos.'})
        if not validate_email(data['email']):
                raise serializers.ValidationError('E-mail inválido, por favor digite um e-mail válido.')
        return data

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