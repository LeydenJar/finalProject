from django.shortcuts import render
from lojas.models import produto, marca, modelo, tração
from lojas import models as modelslojas
from django.core.paginator import Paginator

# Create your views here.
def explore(request):



	""" 
	#if request.method == "GET":
		produtos = produto.objects.all()[:10]
		marcas = marca.objects.all()[:10]
		modelos = modelo.objects.all()[:10]
		trações = tração.objects.all()[:10]
	
	
	#elif request.method == "POST":
		categoria = request.POST.get("categoria")
		valor = request.POST.get("valor")

		pick = models_lojas[categoria].objects.get(nome = valor)


		produtos = produto.objects.filter(models_lojas[categoria] = pick)[:10]
		marcas = marca.objects.all()[:10]
		modelos = modelo.objects.all()[:10]
		trações = tração.objects.all()[:10]

	"""
	

	produtos = produto.objects.all()[:9]
	page = request.GET.get('page')
	print(page)
	paginator = Paginator(produtos, 9)
	produtos = paginator.get_page(page)
	marcas = marca.objects.all()
	modelos = modelo.objects.all()
	trações = tração.objects.all()
	produtos = produto.objects.all()[:9]

	context = {
		'produtos' : produtos,
		'marcas' : marcas,
		'modelos' : modelos,
		'trações' : trações
	}
	

	return render(request, 'explorar/home.html', context)

	
def filtro(request, categoria, chave):

	#if categoria == 'titulo':

	#else:

	model = getattr(modelslojas, categoria)
	pick = model.objects.get(nome = chave)
	
	filters = {
        categoria: pick
    }
    
	produtos = produto.objects.filter(**filters)
	page = request.GET.get('page')
	print(page)
	paginator = Paginator(produtos, 9)
	produtos = paginator.get_page(page)

	marcas = marca.objects.all()
	modelos = modelo.objects.all()
	trações = tração.objects.all()

	context = {
		'produtos' : produtos,
		'marcas' : marcas,
		'modelos' : modelos,
		'trações' : trações
	}
	

	return render(request, 'explorar/home.html', context)


def pagina_do_caminhao(request, chave):
	p = produto.objects.select_related('loja').get(pk = chave)
	
	context={
	'produto' : p
	}
	
	return render(request, 'explorar/produto.html', context)