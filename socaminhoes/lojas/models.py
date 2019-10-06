from django.db import models
from django.contrib.auth.models import User

# Create your models here.




class marca(models.Model):
	nome = models.CharField(max_length = 50)

	def __str__(self):
		return self.nome

	

class tração(models.Model):
	nome = models.CharField(max_length = 50)

	def __str__(self):
		return self.nome

	

class modelo(models.Model):
	nome = models.CharField(max_length = 50)
	marca = models.ForeignKey('marca', on_delete=models.CASCADE)

	def __str__(self):
		return self.nome

	

class ano(models.Model):
	ano = models.PositiveSmallIntegerField()

	def __str__(self):
		return str(self.ano)

	

class implemento(models.Model):
	titulo = models.CharField(max_length = 50)
	loja = models.ForeignKey(User, on_delete=models.CASCADE)

class produto(models.Model):
	titulo = models.CharField(max_length = 50)
	descrição = models.CharField(max_length = 300, blank=True)
	preço = models.DecimalField(max_digits = 11, decimal_places = 2)
	loja = models.ForeignKey(User, on_delete=models.CASCADE)
	marca = models.ForeignKey('marca', on_delete=models.CASCADE)
	modelo = models.ForeignKey('modelo', on_delete=models.CASCADE)
	ano_de_fabricação = models.ForeignKey('ano', on_delete=models.CASCADE, related_name='ano_de_fabricação')
	ano_do_modelo = models.ForeignKey('ano', on_delete=models.CASCADE, related_name='ano_do_modelo')
	tração = models.ForeignKey('tração', on_delete=models.CASCADE)
	quilometragem = models.PositiveIntegerField(blank = True)
	imagem = models.ImageField(upload_to='imagens_dos_produtos', blank=True, null=True)

	def __str__(self):
		return self.titulo


	"""	
	def update(cls, produto):
					
		instance = cls (
		titulo = produto['titulo'],
		descrição = produto['descrição'],
		preço = produto['preço'],
		loja = produto['loja'],
		marca = marca.objects.get(pk=produto['marca']),
		modelo = modelo.objects.get(pk=produto['modelo']),
		ano_de_fabricação = ano.objects.get(pk = produto['ano_de_fabricação']),
		ano_do_modelo = ano.objects.get(pk = produto['ano_do_modelo']),
		tração = tração.objects.get(pk=produto['tração']),
		quilometragem = produto['quilometragem'],
		imagem = produto['imagem'])
		self = instance
		return instance
	"""
	@classmethod
	def create(cls, produto):
		instance = cls(titulo = produto['titulo'], 
						descrição = produto['descrição'], 
						preço = produto['preço'], 
						loja = produto['loja'],
						marca = marca.objects.get(pk=produto['marca']),
						modelo = modelo.objects.get(pk=produto['modelo']),
						ano_de_fabricação = ano.objects.get(pk = produto['ano_de_fabricação']),
						ano_do_modelo = ano.objects.get(pk = produto['ano_do_modelo']),
						tração = tração.objects.get(pk=produto['tração']),
						quilometragem = produto['quilometragem'],
						imagem = produto['imagem']
						 )
		return instance