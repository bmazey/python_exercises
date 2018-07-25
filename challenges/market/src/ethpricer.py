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
        url = 'https://api.kraken.com/0/public/Ticker'
        r = requests.get(url)
        return r

    @staticmethod
    def get_eth_usd_price_response():
        # TODO - implement this method!
        url = 'https://api.kraken.com/0/public/Ticker'
        r = requests.get(url)
        return json.dumps(r.json())

    @staticmethod
    def get_eth_usd_price():
        # TODO - implement this method!
        url = 'https://api.kraken.com/0/public/Ticker?pair=ETHUSD'
        r = requests.get(url)
        return r.json()['result']['XETHZUSD']['o']

    @staticmethod
    def get_eth_cad_price():
        # TODO - implement this method!
        url = 'https://api.kraken.com/0/public/Ticker?pair=ETHCAD'
        r = requests.get(url)
        return r.json()['result']['XETHZCAD']['o']
