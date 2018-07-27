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
        status = requests.get('https://api.kraken.com/0/public/Ticker?pair=XBTUSD')
        return status

    @staticmethod
    def get_btc_usd_price_response():
        response = requests.get('https://api.kraken.com/0/public/Ticker?pair=XBTUSD')
        return json.dumps(response.json())

    @staticmethod
    def get_btc_usd_price():
        xbtusd = requests.get('https://api.kraken.com/0/public/Ticker?pair=XBTUSD')
        return xbtusd.json()['result']['XXBTZUSD']['o']

    @staticmethod
    def get_btc_cad_price():
        xbtcad = requests.get('https://api.kraken.com/0/public/Ticker?pair=XBTCAD')
        return xbtcad.json()['result']['XXBTZCAD']['o']
