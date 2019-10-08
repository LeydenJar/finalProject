from django import forms

from django.contrib.auth.models import User
from .models import produto



class form_produto(forms.ModelForm):
	class Meta:  
		model = produto  
		fields = ['titulo', 'preço', 'imagem', 'marca', 'ano_de_fabricação' ]