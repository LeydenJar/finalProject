from django import forms
from lojas.models import produto



class form_produto(forms.ModelForm):
	class Meta:  
		model = produto  
		fields = ['titulo', 'preço', 'imagem']