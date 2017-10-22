from search import abstract_search
# import requests
from urllib.request import urlopen
import ssl
import json

from time import sleep

class AlphaVantageSearch(abstract_search.AbstractSearch):

    def __init__(self):

        super(AlphaVantageSearch, self).__init__()

        self.base_yahoo_url = 'https://www.alphavantage.co/query?'
        self.API_KEY = 'VE8EDMXOGQR66WUU'
        self.request_rety_count = 2

    def _getHtmlArgs(self, arg_dict):
        tempArgs = ''

        for key, value in arg_dict.items():
            if key != '' and value  != '':
                tempArgs += '{}={}&'.format(key, value)

        # remove the last & symbol if it exists and return
        return tempArgs[:-1]

    def _make_request(self, args_dict):
        # Add api to request
        args_dict['apikey'] = self.API_KEY

        for _ in range(self.request_rety_count):
            url = self.base_yahoo_url + self._getHtmlArgs(args_dict)
            print(url)
            ctx = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)

            request = urlopen(url, context=ctx)
            if request.status != 200:
                continue

            output = request.read()
            return json.loads(output.decode('utf-8'))
        return {}

    def isDirectionalMovementIndexPositive(self, ticker):
        payload = {
            'function': 'DX',
            'symbol': ticker,
            'interval': '30min',
            'time_period': '10',
        }
        response = self._make_request(payload)

        # Return false if we weren't able to communicate with server or response is empty
        if len(response) == 0 or response['Technical Analysis: DX'] == {}:
            return False

        import pdb; pdb.set_trace()


    def process(self, stock):
        print(stock)

        if self.isDirectionalMovementIndexPositive(stock):
            return 1
        else:
            return 0


