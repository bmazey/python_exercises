from challenges.market.src.btcpricer import BtcPricer
from challenges.market.src.ethpricer import EthPricer
import requests
import json


def main():
    # this is for experiments only! test does not look here ...
    response = requests.get('https://api.kraken.com/0/public/Ticker?pair=XBTUSD')
    print(json.loads(response.json()))
    return


if __name__ == '__main__':
    main()
