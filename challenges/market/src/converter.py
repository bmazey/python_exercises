from challenges.market.src.btcpricer import BtcPricer
from challenges.market.src.ethpricer import EthPricer
import requests

def main():
    # this is for experiments only! test does not look here ...
    r = requests.get('https://api.kraken.com/0/public/Ticker?pair=XBTUSD')
    print(r)


if __name__ == '__main__':
    main()
