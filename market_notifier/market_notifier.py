from worst_performers import csi_market_worst_performers
from worst_performers import yahoo_worst_performers
from search import alpha_vantage_search

class marketNotifier(object):
	def __init__(self):
		#self.csi_market_worst = csi_market_worst_performers.csiMarketWorstPerformers()
		self.yahoo_worst = yahoo_worst_performers.yahooWorstPerformers()
		self.alpha_search = alpha_vantage_search.AlphaVantageSearch()

		self.BUY_PERCENT = .80
		#self.search           = yahoo_search.YahooSearch()

	def getAllWorstPerformers(self):
		stocks = []
		# stocks.extend(self.csi_market_worst.getWorstDailyPerformers())
		stocks.extend(self.yahoo_worst.getWorstDailyPerformers())
		return stocks

	def is_buy(self, stocks):
		current_percent_buy = []

		current_percent_buy.append(self.alpha_search.process(stocks))
		#current_percent_buy.append(self.search.process(stocks))

		avg_percent = sum(current_percent_buy) / len(current_percent_buy)
		return avg_percent > self.BUY_PERCENT


	def main(self):
		stocks_to_buy = []

		stocks = self.getAllWorstPerformers()
		for stock in stocks:
			if self.is_buy(stock):
				stocks_to_buy.append(stock)


		notify(stocks)

if __name__ == '__main__':
	marketNotifier().main()
