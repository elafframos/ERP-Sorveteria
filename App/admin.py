from django.contrib import admin
from .models import Profile, Produto, Venda

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'cargo')
    search_fields = ('user__username', 'cargo')

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'codigo', 'quantidade', 'preco')
    search_fields = ('nome', 'codigo')

@admin.register(Venda)
class VendaAdmin(admin.ModelAdmin):
    list_display = ('produto', 'quantidade_vendida', 'metodo', 'data_venda')
    search_fields = ('produto__nome', 'metodo')
    list_filter = ('metodo', 'data_venda')
    readonly_fields = ('data_venda',)

