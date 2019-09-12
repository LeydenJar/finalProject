from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import produto

class NewRegistrationForm(UserCreationForm):
	email = forms.EmailField()
	username = forms.CharField(label="Loja", max_length=100)
	

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

class form_produto(forms.ModelForm):
	class Meta:  
		model = produto  
		fields = ['titulo', 'preço', 'imagem', 'marca', 'ano_de_fabricação' ]