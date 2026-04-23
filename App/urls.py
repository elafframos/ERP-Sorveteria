from django.conf import settings
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProdutoViewSet, VendaViewSet, OperadoresViewSet

router = DefaultRouter()
router.register(r'produtos', ProdutoViewSet)
router.register(r'vendas', VendaViewSet)
router.register(r'operadores', OperadoresViewSet, basename='operador')

urlpatterns = [
    # Aqui você pode adicionar as URLs para suas views
    path('', include(router.urls)),
] 