from django.urls import path
from explore.views import explore

urlpatterns = [
	path('', explore, name='home')

]