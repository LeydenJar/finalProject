from django.test import TestCase, Client
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from users.models import User
from django.core.management import call_command
from lojas.models import produto, marca, tração, modelo, ano, implemento
from selenium import webdriver
import pathlib
import os
from time import sleep
#from django.conf import settings


# Create your tests here.
class MyTests(TestCase):
	def setUp(self):

		self.user = User.objects.create_user(username='testuser', password='12345')
		self.client = Client()
		
		for i in range(1990, 2020):
			ano.objects.create(ano=i)
		
		call_command('loaddata', 'socaminhoes/fixtures.json', verbosity=0)



	def teste_numero_trações(self):
		a = tração.objects.all().count()
		self.assertEqual(a, 4)

	def teste_numero_anos(self):
		a = ano.objects.all().count()
		self.assertEqual(a, 30)

	def teste_numero_marcas(self):
		a = marca.objects.all().count()
		self.assertEqual(a, 4)

	def teste_numero_modelos(self):
		a= modelo.objects.all().count()
		
		self.assertEqual(a, 2)


	def teste_home_page(self):
		c = Client()
		response=self.client.get("/")
		self.assertEqual(response.status_code, 200)
		self.assertEqual(len(response.context['produtos']), 0)
		self.assertEqual(len(response.context['marcas']), 4)

	def teste_pagina_administrador(self):
		
		response=self.client.get("/admin/")
		self.assertEqual(response.status_code, 200)

	def teste_criar_produto(self):
		dicionario = {
					'titulo': 'meuproduto',
					'descrição': '', 
					'preço': 10000,
					'marca' : 1,
					'modelo' : 1,
					'ano_de_fabricação' : 1,
					'ano_do_modelo' : 1,
					'tração' : 1,
					'quilometragem' : '',
					}
		login = self.client.login(username='testuser', password='12345')
		response = self.client.post('/admin/novo_produto', dicionario)
		print(produto.objects.all())
		self.assertEqual(len(produto.objects.all()), 1)
		self.assertEqual(response.status_code, 200)
		

		


	


	#login = self.client.login(username='testuser', password='12345') url_do_arquivo("templates/admin/home_admin.html")

class testes_selenium(StaticLiveServerTestCase):
	def setUp(self):
		self.client = Client()
		self.user = User.objects.create_user(username='testuser', password='12345')
		self.superUser = User.objects.create_superuser(username='testSuperUser', email="email@email.com",password="12345")

		self.client.login(username='testuser', password='12345')
		self.cookie_user = self.client.cookies['sessionid']
		
		self.browser = webdriver.Chrome()



		

	def teste_pagina_administrador(self):
		
		self.browser.get(self.live_server_url + '/admin')
		self.assertEqual(self.browser.title, "Só Caminhões - Admin")
		erro = self.browser.find_element_by_id('erro_login')
		self.assertTrue(erro)
		sleep(5)

		self.browser.get(self.live_server_url + '/admin/')  #selenium will set cookie domain based on current page domain
		self.browser.add_cookie({'name': 'sessionid', 'value': self.cookie_user.value, 'secure': False, 'path': '/'})
		self.browser.refresh() #need to update page for logged in user
		self.browser.get(self.live_server_url + '/admin/')
		self.browser.refresh()
		sleep(5)
		try:
			erro = self.browser.find_element_by_id('erro_login')
			print(erro)
		except:
			erro = False
		
		self.assertFalse(erro)


	def teste_pagina_superadmin(self):

		self.browser.delete_cookie('sessionid')
		self.browser.get(self.live_server_url +"/superadmin")
		try:
			t = self.browser.find_element_by_css_selector("body.login")
		except:
			t=False
		self.assertTrue(t)

		self.browser.add_cookie({'name': 'sessionid', 'value': self.cookie_user.value, 'secure': False, 'path': '/'})
		self.browser.refresh()
		try:
			t = self.browser.find_element_by_css_selector(".login")
		except:
			t=False

		self.assertTrue(t)

		self.client.logout()
		self.client.login(username='testSuperUser', password="12345")
		self.cookie_superuser = self.client.cookies['sessionid']
		self.browser.delete_cookie('sessionid')
		self.browser.add_cookie({'name': 'sessionid', 'value': self.cookie_superuser.value, 'secure': False, 'path': '/'})
		self.browser.refresh()
		try:
			t = self.browser.find_element_by_css_selector(".login")
		except:
			t=False
		self.assertFalse(t)
