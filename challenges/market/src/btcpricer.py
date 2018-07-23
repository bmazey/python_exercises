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
        return requests.get('https://api.kraken.com/0/public/Ticker')

    @staticmethod
    def get_btc_usd_price_response():
        return requests.get('https://api.kraken.com/0/public/Ticker').text

    @staticmethod
    def get_btc_usd_price():
        r = requests.get('https://api.kraken.com/0/public/Ticker', params={'pair': 'XBTUSD'})
        return json.loads(r.text)['result']['XXBTZUSD']['o']

    @staticmethod
    def get_btc_cad_price():
        r = requests.get('https://api.kraken.com/0/public/Ticker', params={'pair': 'XBTCAD'})
        return json.loads(r.text)['result']['XXBTZCAD']['o']
