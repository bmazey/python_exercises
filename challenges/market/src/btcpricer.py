import requests
import json


class BtcPricer:
    def __init__(self):
        # you will need to research the 'requests' module
        # you will need to read documentation: https://www.kraken.com/help/api
        # meet my friend json: json.org
        # do nothing in this constructor (normally security goes here ...)
        return

    @staticmethod
    def get_btc_usd_price_status():
        s = requests.get('https://api.kraken.com/0/public/Ticker')
        return s

    @staticmethod
    def get_btc_usd_price_response():
        o = requests.get('https://api.kraken.com/0/public/Ticker').text
        return o

    @staticmethod
    def get_btc_usd_price():
        price = requests.get('https://api.kraken.com/0/public/Ticker', params={'pair': 'XBTUSD'})
        price = json.loads(price.text)['result']['XXBTZUSD']['o']
        return price

    @staticmethod
    def get_btc_cad_price():
        price = requests.get('https://api.kraken.com/0/public/Ticker', params={'pair': 'XBTCAD'})
        price = json.loads(price.text)['result']['XXBTZCAD']['o']
        return price
