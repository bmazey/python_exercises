from challenges.market.src.btcpricer import BtcPricer
from challenges.market.src.ethpricer import EthPricer
import requests
import json

def main():
    # this is for experiments only! test does not look here ...
    r = requests.get('https://api.kraken.com/0/public/Ticker?pair=XBTUSD')
    mydata = json.loads(r.text)
    price = mydata["result"]["XXBTZUSD"]["a"][0]
    print(r)

    return


if __name__ == '__main__':
    main()
