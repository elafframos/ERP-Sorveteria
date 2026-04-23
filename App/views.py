from rest_framework import viewsets, status, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes # Importe permission_classes
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User # Importe o User aqui em cima
from .models import Produto, Venda
from .serializer import ProdutoSerializer, VendaSerializer, UserSerializer
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt

class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    permission_classes = [permissions.IsAuthenticated]

class VendaViewSet(viewsets.ModelViewSet):
    queryset = Venda.objects.all()
    serializer_class = VendaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=isinstance(request.data, list))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OperadoresViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # Opcional: Se quiser que o login carregue os nomes, deixe AllowAny aqui
    permission_classes = [permissions.AllowAny]

@api_view(['GET'])
@permission_classes([permissions.AllowAny]) # CHAVE DO SUCESSO: Permite carregar a lista no Login
def listar_operadores(request):
    usuarios = User.objects.all().values('id', 'username')
    return Response(usuarios)

@api_view(['POST'])
@ensure_csrf_cookie
@permission_classes([permissions.AllowAny])
def login_operador(request):
    username = request.data.get('username')
    password = request.data.get('password')
    
    user = authenticate(username=username, password=password)
    
    if user is not None:
        login(request, user)
        request.session.modified = True
        return Response({"mensagem": "Login realizado!", "id": user.id}, status=status.HTTP_200_OK)
    else:
        return Response({"erro": "Senha incorreta ou usuário inválido"}, status=status.HTTP_401_UNAUTHORIZED)
    
@api_view(['POST'])
def logout_operador(request):
    logout(request) # Remove a sessão do banco de dados e limpa o cookie
    return Response({"mensagem": "Logout realizado com sucesso!"}, status=status.HTTP_200_OK)