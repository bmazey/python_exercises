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
        response = requests.get('https://api.kraken.com/0/public/Ticker?pair=XBTUSD')
        return response

    @staticmethod
    def get_btc_usd_price_response():
        r = requests.get('https://api.kraken.com/0/public/Ticker?pair=XBTUSD')
        return r.text

    @staticmethod
    def get_btc_usd_price():
        r = requests.get('https://api.kraken.com/0/public/Ticker?pair=XBTUSD')
        return r.json().get('result').get('XXBTZUSD').get('o')

    @staticmethod
    def get_btc_cad_price():
        r = requests.get('https://api.kraken.com/0/public/Ticker?pair=XBTCAD')
        return r.json().get('result').get('XXBTZCAD').get('o')