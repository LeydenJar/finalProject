from django.urls import path
from .views import home_admin, novo_produto, meus_produtos

urlpatterns = [
	path('', home_admin, name='home_admin'),
	path('novo_produto', novo_produto, name='novo_produto'),
	path('meus_produtos', meus_produtos, name='meus_produtos')
]