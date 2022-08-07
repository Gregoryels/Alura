from rest_framework import serializers
from orcamentos.models import Despesas, Receitas
from rest_framework.validators import UniqueForMonthValidator

class DespesasSerializer(serializers.ModelSerializer):
    def validate_valor(self, valor):
        if valor <= 0:
            raise serializers.ValidationError("O valor deve ser maior do que zero")

    class Meta:
        model = Despesas
        fields = ['descricao', 'valor', 'data']
        validators = [UniqueForMonthValidator(
            queryset=Despesas.objects.all(),
            field='descricao',
            date_field='data',
            message='Já existe uma despesa com essa descrição para esse mês')]

class ReceitasSerializer(serializers.ModelSerializer):
    def validate_valor(self, valor):
        if valor <= 0:
            raise serializers.ValidationError("O valor deve ser maior do que zero")

    class Meta:
        model = Receitas
        fields = ['descricao', 'valor', 'data']
        validators = [UniqueForMonthValidator(
            queryset=Receitas.objects.all(),
            field='descricao',
            date_field='data',
            message='Já existe uma despesa com essa descrição para esse mês')]