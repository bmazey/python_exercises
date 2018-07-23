import requests
import json


class EthPricer:
    def __init__(self):
        # you will need to research the 'requests' module
        # you will need to read documentation: https://www.kraken.com/help/api
        # meet my friend json: json.org
        # do nothing in this constructor (normally security goes here ...)
        return

    @staticmethod
    def get_eth_usd_price_status():
        # TODO - implement this method!
        return requests.get('https://api.kraken.com/0/public/Ticker')

    @staticmethod
    def get_eth_usd_price_response():
        # TODO - implement this method!
        return requests.get('https://api.kraken.com/0/public/Ticker').text

    @staticmethod
    def get_eth_usd_price():
        # TODO - implement this method!
        request = requests.get('https://api.kraken.com/0/public/Ticker', params={'pair': 'ETHUSD'})
        return json.loads(request.text)['result']['XETHZUSD']['o']

    @staticmethod
    def get_eth_cad_price():
        # TODO - implement this method!
        request = requests.get('https://api.kraken.com/0/public/Ticker', params={'pair': 'ETHCAD'})
        return json.loads(request.text)['result']['XETHZCAD']['o']
