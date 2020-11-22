import os
import requests


class HttpParser:

	def __init__(self, url):
		
		self.url = url
		self.PATH_OUTPUT = 'outputs/'
		self.parseFromUrl()


	def parseFromUrl(self):

		response = requests.get(self.url)

		self.response = response


	def seveToFile(self, name='output', expansion='html'):

		try:
			with open(f'{self.PATH_OUTPUT}{name}.{expansion}', 'w') as file:

				file.write(self.response.text)

		except FileNotFoundError:

			os.mkdir(self.PATH_OUTPUT)

			with open(f'{self.PATH_OUTPUT}{name}.{expansion}', 'w') as file:

				file.write(self.response.text)


	def __str__(self):

		return self.response.text


httpParser = HttpParser('https://school10perm.ru/')
httpParser.seveToFile(name='test', expansion='html')