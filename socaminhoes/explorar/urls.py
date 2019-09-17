from django.urls import path
from .views import explore, filtro, pagina_do_caminhao

urlpatterns = [
	path('', explore, name='home'),
	path('caminhao/<chave>', pagina_do_caminhao, name='pagina_do_caminhao'),
	path('filtro/<categoria>/<chave>', filtro, name='filtro')
]