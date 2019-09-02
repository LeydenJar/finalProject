from django.urls import path
from lojas.views import registro
from django.contrib.auth import views as auth_views

urlpatterns = [
	path('registro', registro, name = 'registro'),
	path('login', auth_views.LoginView.as_view(template_name='lojas/login.html'), name="login"),
	path('logout', auth_views.LogoutView.as_view(template_name='base.html'), name='logout')
]