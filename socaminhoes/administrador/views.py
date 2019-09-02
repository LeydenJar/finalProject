from django.shortcuts import render
from .forms import form_produto
from lojas import models
from django.contrib import messages
from lojas.serializers import serializar_produto
from django.shortcuts import get_object_or_404

# Create your views here.
def home_admin(request):
	return render(request, 'admin/home_admin.html')

def novo_produto(request):
	if request.method == 'GET':
		return render(request, 'admin/novo_produto.html', {'form' : form_produto})
	elif request.method == 'POST':

		try:
			
			img = request.POST.get('imagem')
			print(img)
			print(request.FILES)
			produto = {
				'titulo' : request.POST.get('titulo'),
				'preço' : request.POST.get('preço'),
				'imagem' : request.FILES['imagem'],
				'loja' : request.user.username
			}
			print(type(produto["imagem"]))
				
			instance = models.produto.create(produto)
			instance.save()

			messages.success(request, 'Produto adicionado com sucesso!!')
			
		except:
			messages.error(request, 'Erro de servidor!!')
		return render(request, 'admin/novo_produto.html', {'form' : form_produto})

	

def meus_produtos(request):
	produtos = models.produto.objects.filter(loja = request.user)
	""" 
	lista_produtos = []
	for p in produtos:
		lista_produtos.append(p)
	serial = serializar_produto(lista_produtos).data
	serial2 = serializar_produto(list(produtos)).data
	print(produtos)
	print(serial)
	print(serial2)
	"""
	return render(request, 'admin/meus_produtos.html', {'produtos' : produtos})