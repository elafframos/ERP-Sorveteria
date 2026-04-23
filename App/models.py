from django.db import models
from django.contrib.auth.models import User

# O Profile agora só guarda informações adicionais, sem repetir a senha
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cargo = models.CharField(max_length=50, default="Atendente")

    def __str__(self):
        return self.user.username

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    codigo = models.CharField(max_length=50, unique=True) # Unique evita códigos duplicados
    quantidade = models.PositiveIntegerField(default=0) # Garante que não tenha estoque negativo
    preco = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return self.nome

class Venda(models.Model):
    # Relaciona a venda ao que foi vendido
    METODO_PAGAMENTO = [
        ('PIX', 'Pix'),
        ('DIN', 'Dinheiro'),
        ('DEB', 'Débito'),
        ('CRE', 'Crédito'),
    ]
    
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT)
    quantidade_vendida = models.PositiveIntegerField()
    metodo = models.CharField(max_length=3, choices=METODO_PAGAMENTO)
    data_venda = models.DateTimeField(auto_now_add=True)
    operador = models.CharField(max_length=50)
    valor_recebido = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    troco = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.quantidade_vendida}x {self.produto.nome} - {self.metodo}"
    
    def save(self, *args, **kwargs):
        # Apenas subtrai, sem medo, porque o produto já saiu do freezer
        produto = self.produto
        produto.quantidade -= self.quantidade_vendida
        produto.save()
        
        super().save(*args, **kwargs)