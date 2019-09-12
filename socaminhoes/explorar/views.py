from django.shortcuts import render
from lojas.models import produto, marca, modelo, tração
from lojas import models as modelslojas

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
	

	produtos = produto.objects.all()[:10]
	marcas = marca.objects.all()[:10]
	modelos = modelo.objects.all()[:10]
	trações = tração.objects.all()[:10]

	context = {
		'produtos' : produtos,
		'marcas' : marcas,
		'modelos' : modelos,
		'trações' : trações
	}
	

	return render(request, 'explorar/home.html', context)

	
def filtro(request, categoria, chave):

	model = getattr(modelslojas, categoria)
	pick = model.objects.get(nome = chave)
	
	filters = {
        categoria: pick
    }
    
	produtos = produto.objects.filter(**filters)[:10]


	marcas = marca.objects.all()[:10]
	modelos = modelo.objects.all()[:10]
	trações = tração.objects.all()[:10]

	context = {
		'produtos' : produtos,
		'marcas' : marcas,
		'modelos' : modelos,
		'trações' : trações
	}
	

	return render(request, 'explorar/home.html', context)
