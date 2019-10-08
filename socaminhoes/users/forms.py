from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import User

class NewRegistrationForm(UserCreationForm):
	email = forms.EmailField()
	username = forms.CharField(label="Loja", max_length=100)
	telefone = forms.CharField(label="Telefone", max_length=15)
	celular = forms.CharField(label="Celular", max_length=15)
	cidade = forms.CharField(label='Cidade', max_length=30)
	
	class Meta:
		model = User
		fields = ('username', 'email')


class NewUserChangeForm(UserChangeForm):

	class Meta:
		model = User
		fields = ('username', 'email')


