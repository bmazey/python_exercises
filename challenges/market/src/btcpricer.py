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
        # gets price status
        req = requests.get('https://api.kraken.com/0/public/Ticker?pair=XBTUSD')
        return req

    @staticmethod
    def get_btc_usd_price_response():
        # gets response text
        req = requests.get('https://api.kraken.com/0/public/Ticker?pair=XBTUSD')
        return req.text

    @staticmethod
    def get_btc_usd_price():
        # gets bitcoin price in USD
        req = requests.get('https://api.kraken.com/0/public/Ticker?pair=XBTUSD')
        mydata = json.loads(req.text)
        price = mydata["result"]["XXBTZUSD"]["o"]
        return price

    @staticmethod
    def get_btc_cad_price():
        # gets bitcoin price in Canadian dollars
        req = requests.get('https://api.kraken.com/0/public/Ticker?pair=XBTCAD')
        mydata = json.loads(req.text)
        price = mydata["result"]["XXBTZCAD"]["o"]
        return price
