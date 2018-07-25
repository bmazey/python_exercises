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
        req = requests.post('https://api.kraken.com/0/public/Ticker')
        return req

    @staticmethod
    def get_eth_usd_price_response():
        # TODO - implement this method!
        req = requests.post('https://api.kraken.com/0/public/Ticker').text
        return req

    @staticmethod
    def get_eth_usd_price():
        # TODO - implement this method!
        price = requests.post('https://api.kraken.com/0/public/Ticker', params={'pair': 'ETHUSD'})
        price = json.loads(price.text)['result']['XETHZUSD']['o']
        return price

    @staticmethod
    def get_eth_cad_price():
        # TODO - implement this method!
        price = requests.post('https://api.kraken.com/0/public/Ticker', params={'pair': 'ETHCAD'})
        price = json.loads(price.text)['result']['XETHZCAD']['o']
        return price


