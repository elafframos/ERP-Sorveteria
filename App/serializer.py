from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Profile, Produto, Venda

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'

class VendaSerializer(serializers.ModelSerializer):
    nome = serializers.ReadOnlyField(source='produto.nome')
    codigo = serializers.ReadOnlyField(source='produto.codigo')
    operador = serializers.CharField(max_length=50)
    valor_recebido = serializers.DecimalField(max_digits=10, decimal_places=2)
    troco = serializers.DecimalField(max_digits=10, decimal_places=2)
    
    class Meta:
        model = Venda
        fields = [
            'id', 'quantidade_vendida', 'metodo', 'data_venda', 
            'produto', 'nome', 'codigo', 'operador', 
            'valor_recebido', 'troco'
        ]

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']