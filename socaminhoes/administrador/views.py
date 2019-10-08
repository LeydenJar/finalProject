from django.shortcuts import render, redirect
from .forms import form_produto
from lojas import models
from django.contrib import messages
from lojas.serializers import serializar_produto
from django.shortcuts import get_object_or_404, redirect
from django.http import Http404, JsonResponse
from users.models import User
from users.forms import NewUserChangeForm, form_de_mudar_dados, form_de_mudar_senha
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required

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

"""def minha_conta(request):
	if request.method == "GET":
		form = NewUserChangeForm()
		return render(request, 'admin/minha_conta.html', {'form' : form})
	elif request.method == "POST":
		raise Http404('still not built it')
	else:
		raise Http404('Invalid request method')"""

def mudar_dados(request):
	if request.method == "GET":
		form = form_de_mudar_dados()
		return render(request, 'admin/mudar_dados.html', {'form':form})
	elif request.method == "POST":
		form=form_de_mudar_dados(data=request.POST, instance=request.user)
		
		if form.is_valid():

			user = form.save(commit=False)
			user.save()
			messages.success(request, "Conta alterada com sucesso")
		else:
			messages.error(request, "Desculpe, houve um problema na autenticação dos dados!")
		return render(request, 'admin/home_admin.html')
	else:
		raise Http404("Invalid Request Method")
	
@login_required
def mudar_senha(request):
	form = form_de_mudar_senha(user=request.user, data=request.POST or None)
	if form.is_valid():
		form.save()
		form_de_mudar_senha(request, form.user)
		return redirect('/')
	return render(request, 'admin/mudar_senha.html', {'form': form})