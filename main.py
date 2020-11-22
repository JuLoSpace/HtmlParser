import requests


class HttpParser:

	def __init__(self, url):
		
		self.url = url
		self.parseFromUrl()


	def parseFromUrl(self):

		response = requests.get(self.url)

		self.response = response


	def __str__(self):

		return self.response.text


httpParser = HttpParser('https://school10perm.ru/')
print(str(httpParser))