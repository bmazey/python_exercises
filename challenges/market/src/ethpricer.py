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
        _status = requests.get('https://api.kraken.com/0/public/Ticker?pair=ETHUSD')
        return _status

    @staticmethod
    def get_eth_usd_price_response():
        _response = requests.get('https://api.kraken.com/0/public/Ticker?pair=ETHUSD')
        return json.dumps(_response.json())

    @staticmethod
    def get_eth_usd_price():
        ethusd = requests.get('https://api.kraken.com/0/public/Ticker?pair=ETHUSD')
        return ethusd.json()['result']['XETHZUSD']['o']

    @staticmethod
    def get_eth_cad_price():
        ethcad = requests.get('https://api.kraken.com/0/public/Ticker?pair=ETHCAD')
        return ethcad.json()['result']['XETHZCAD']['o']
