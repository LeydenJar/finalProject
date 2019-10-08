from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from users.forms import NewRegistrationForm


# Create your views here.
def registro(request):
	if request.method == "GET":
		form = NewRegistrationForm()
		return render(request, "lojas/registro.html", {"form" : form})

	else:
		form = NewRegistrationForm(request.POST)
		if form.is_valid():
			try:
				user = form.save()
				user.save()
				username = form.cleaned_data.get("username")
				messages.success(request, f"Conta criada para {username}!")
				return redirect("login")
			except:
				messages.error(request, "Aconteceu um erro ao criar a conta :(")
				return render(request, "lojas/registro.html", {"form" : form})
		else:
			messages.error(request, 'dados inválidos')
			return render(request, "lojas/registro.html", {"form" : form})