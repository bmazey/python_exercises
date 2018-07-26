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
        # gets price status
        req = requests.get('https://api.kraken.com/0/public/Ticker?pair=ETHUSD')
        return req

    @staticmethod
    def get_eth_usd_price_response():
        # gets response
        req = requests.get('https://api.kraken.com/0/public/Ticker?pair=ETHUSD')
        return req.text

    @staticmethod
    def get_eth_usd_price():
        # gets ethereum price in USD
        req = requests.get('https://api.kraken.com/0/public/Ticker?pair=ETHUSD')
        mydata = json.loads(req.text)
        price = mydata["result"]["XETHZUSD"]['o']
        return price

    @staticmethod
    def get_eth_cad_price():
        # gets ethereum price in Canadian dollars
        req = requests.get('https://api.kraken.com/0/public/Ticker?pair=ETHCAD')
        mydata = json.loads(req.text)
        price = mydata["result"]["XETHZCAD"]['o']
        return price
