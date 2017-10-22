import urllib

class AbstractSearch(object):
	def __init__(self):
		pass

	def isInsidersBuying(self):
		return Exception("Not Implemented")

	def isRecomentedByAynlists(self):
		return Exception("Not Implemented")

	def url_encode(self, temp_URl):
		return urllib.urlencode(temp_URl)
