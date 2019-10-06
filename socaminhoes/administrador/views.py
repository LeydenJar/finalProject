from django.shortcuts import render
from .forms import form_produto
from lojas import models
from django.contrib import messages
from lojas.serializers import serializar_produto
from django.shortcuts import get_object_or_404, redirect
from django.http import Http404, JsonResponse
from django.contrib.auth.models import User
# Create your views here.
def home_admin(request):
	return render(request, 'admin/home_admin.html')

def novo_produto(request):
	if request.method == 'GET':
		return render(request, 'admin/novo_produto.html', {'form' : form_produto})


	elif request.method == 'POST':
		try:
			
			#img = request.POST.get('imagem')

			produto = {
				'titulo' : request.POST.get('titulo'),
				'descrição' : request.POST.get('descrição'),
				'preço' : request.POST.get('preço'),
				'loja' : request.user,
				'marca' : request.POST.get("marca"),
				'modelo' : request.POST.get("modelo"),
				'ano_de_fabricação' : request.POST.get("ano_de_fabricação"),
				'ano_do_modelo' : request.POST.get("ano_do_modelo"),
				'tração' : request.POST.get("tração"),
				'quilometragem' : request.POST.get("quilometragem"),
				
				
			}
			try:
				produto['imagem'] = request.FILES['imagem']
			except:
				produto['imagem'] = None

			if not produto['quilometragem']:
				produto['quilometragem']=False

			
				

				
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

def excluir_produto(request):
	if request.method == 'POST':
		pk = request.POST.get('pk')
		print(pk)
		produto = models.produto.objects.get(pk = pk)
		produto.delete()
		return JsonResponse({'success':True})
	else:
		raise Http404('Error: Invalid request method')


def editar_produto(request, pk):
	
	produto = models.produto.objects.get(pk=pk)
	print("user: " + request.user.username + "loja: " +produto.loja.username)
	if produto.loja != request.user:
		raise Http404('product is not yours!')


	if request.method=='POST':
		info = {
			'titulo' : request.POST.get('titulo'),
			'descrição' : request.POST.get('descrição'),
			'preço' : request.POST.get('preço'),
			#'loja' : request.user,
			'marca' : request.POST.get("marca"),
			'modelo' : request.POST.get("modelo"),
			'ano_de_fabricação' : request.POST.get("ano_de_fabricação"),
			'ano_do_modelo' : request.POST.get("ano_do_modelo"),
			'tração' : request.POST.get("tração"),
			'quilometragem' : request.POST.get("quilometragem"),	
			}
		try:
			info['imagem'] = request.FILES['imagem']
		except:
			print('beHappy')

		if not info['quilometragem']:
			info['quilometragem']=False

		
		models.produto.objects.filter(pk=produto.id).update(**info)
		return redirect('meus_produtos')
	    
	else:
		get_object_or_404(models.produto, pk=pk)
		
		return render(request, 'admin/editar_produto.html', {'form' : form_produto, 'pk':pk})