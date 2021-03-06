from django.urls import path
from .views import home_admin, novo_produto, meus_produtos, excluir_produto, editar_produto, mudar_dados, mudar_senha

urlpatterns = [
	path('', home_admin, name='home_admin'),
	path('novo_produto', novo_produto, name='novo_produto'),
	path('meus_produtos', meus_produtos, name='meus_produtos'),
	path('excluir_produto', excluir_produto, name='excluir_produto'),
	path('editar_produto/<pk>', editar_produto, name='editar_produto'),
	#path('minha_conta', minha_conta, name='minha_conta'),
	path('mudar_dados', mudar_dados, name='mudar_dados'),
	path('mudar_senha', mudar_senha, name='mudar_senha')
]