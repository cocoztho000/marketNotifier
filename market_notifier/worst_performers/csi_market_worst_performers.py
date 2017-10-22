from worst_performers import abstract_worst_performers as awp
import requests
from lxml import html

class csiMarketWorstPerformers(awp.abstractWorstPerformers):

    def getWorstDailyPerformers(self):
        print('Getting CSI Market Worst')

        page = requests.get('http://csimarket.com/markets/Stocks.php', verify=False)
        tree = html.fromstring(page.content)

        worst_performers_td = tree.xpath('//td[@class="padl3"]')

        if len(worst_performers_td) == 0:
            print('ERROR: Failed to find worst performers table')
            return


        worst_performers_trs = worst_performers_td[0].xpath('//tr[@class="hov"]')

        for worst_performers_tr in worst_performers_trs:
            children = worst_performers_tr.getchildren()

            if len(children) != 2:
                print('Weird this table row has more than 2 items: ' + children.text_content())

            company_name = self.removeUnicodeFromString(children[0].text_content())
            percent      = self.removeUnicodeFromString(children[1].text_content())

