

class abstractWorstPerformers(object):

	def __init__(self):
		pass

	def getWorstDailyPerformers(self):
		raise Exception("Not Implimented")

	def removeUnicodeFromString(self, tempStr):
		return tempStr.encode('ascii', 'ignore').strip()
