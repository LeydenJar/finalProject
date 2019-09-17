from django import forms
from lojas.models import produto



class form_produto(forms.ModelForm):
	class Meta:  
		model = produto  
		fields = ['titulo', 'descrição', 'preço', 'marca', 'modelo', 'ano_de_fabricação', 'ano_do_modelo', 'tração', 'quilometragem', 'imagem']