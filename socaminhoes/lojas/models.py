from django.db import models

# Create your models here.
class produto(models.Model):
	titulo = models.CharField(max_length = 50)
	preço = models.DecimalField(max_digits = 11, decimal_places = 2)
	imagem = models.ImageField(upload_to='imagens_dos_produtos', blank=True)
	loja = models.CharField(max_length = 50, null=True)

	def __str__(self):
		return self.titulo

	@classmethod
	def create(cls, produto):
		instance = cls(titulo = produto['titulo'], preço = produto['preço'], imagem = produto['imagem'], loja = produto['loja'])
		return instance

