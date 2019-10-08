from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
	telefone = models.CharField(max_length=15)
	celular = models.CharField(max_length=15)
	cidade = models.CharField(max_length=30)
	class Meta:
		db_table = 'auth_user'
    # add additional fields in here
