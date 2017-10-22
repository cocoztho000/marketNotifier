from search import abstract_search
import requests
from time import sleep

class YahooSearch(abstract_search.AbstractSearch):
	def __init__(self):
		self.base_yahoo_url = 'https://finance.yahoo.com/quote?p='

	def isInsidersBuying(self, page_text):
		return Exception("Not Implemented")

	def isRecomentedByAynlists(self, page_text):
		return Exception("Not Implemented")


	def process(self, stocks):
		print(stocks)

		recommended_stocks = []

		for stock in stocks:
			request = requests.get(self.url_encode(self.base_yahoo_url + stocks.strip()))

			is_insiders_buying = self.isInsidersBuying(request.text)
			is_recommented_by_aynlysts = self.isRecomentedByAynlists(request.text)

			# TODO: this logs should be moved into their cooresponding functions
			if is_insiders_buying:
				print('Insiders are buying')

			if is_recommented_by_aynlysts:
				print('Recomended by anylists')

			if is_insiders_buying and is_recommented_by_aynlysts:
				recommended_stocks.append(stock)

		return recommended_stocks
