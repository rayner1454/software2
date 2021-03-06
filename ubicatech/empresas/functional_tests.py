#Realizando mis test con Selenium
#Importamos el modulo de Pruebas Unitarias
import unittest
from selenium import webdriver

class UbicatechFunctionalTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)
	
	def tearDown(self):
		self.browser.quit()

	def test_home_page_es_acerca_ubicatech(self):
		self.browser.get('http://localhost:8000')
		self.assertIn('Django', self.browser.title)

if __name__ == '__main__':
	unittest.main()