from django.contrib import admin
from .models import produto, ano, modelo, marca, tração, implemento

# Register your models here.
admin.site.register(produto)
admin.site.register(ano)
admin.site.register(modelo)
admin.site.register(marca)
admin.site.register(tração)
admin.site.register(implemento)