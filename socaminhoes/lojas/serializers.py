from rest_framework import serializers
from .models import produto

class serializar_produto(serializers.ModelSerializer):
	class Meta:
		model = produto
		fields = '__all__'
