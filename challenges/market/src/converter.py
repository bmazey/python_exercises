from challenges.market.src.btcpricer import BtcPricer
from challenges.market.src.ethpricer import EthPricer
import requests
import json


def main():
    url = 'https://api.kraken.com/0/public/Ticker?pair=XBTUSD'
    r = requests.get(url)
    print(r.json()['result']['XXBTZUSD']['o'])


if __name__ == '__main__':
    main()
