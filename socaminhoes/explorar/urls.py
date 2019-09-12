from django.urls import path
from .views import explore, filtro

urlpatterns = [
	path('', explore, name='home'),
	path('<categoria>/<chave>', filtro, name='filtro')

]