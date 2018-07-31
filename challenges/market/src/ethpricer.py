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
        return requests.get('https://api.kraken.com/0/public/Ticker')

    @staticmethod
    def get_eth_usd_price_response():
        data = {'pair': 'ETHUSD'}
        x = requests.get('https://api.kraken.com/0/public/Ticker', data)
        return requests.get('https://api.kraken.com/0/public/Ticker').text

    @staticmethod
    def get_eth_usd_price():
        data = {'pair': 'ETHUSD'}
        r = requests.get('https://api.kraken.com/0/public/Ticker', params=data)
        return json.loads(r.text)['result']['XETHZUSD']['o']

    @staticmethod
    def get_eth_cad_price():
        data = {'pair': 'ETHCAD'}
        r = requests.get('https://api.kraken.com/0/public/Ticker', params=data)
        return json.loads(r.text)['result']['XETHZCAD']['o']
