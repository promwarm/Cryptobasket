import requests
import json

# Doucmentation: https://min-api.cryptocompare.com

def scrape(coin, currency):
    # Coin max-length = 10
    # You can enter multiple currencties, comma seperated
    appname = 'Crytpobasket_by_promwarm@gmail.com'
    url = "https://min-api.cryptocompare.com/data/price?fsym={0}&tsyms={1}&extraParms={2}".format(coin, currency, appname)
    response = requests.get(url)
    if response.status_code == 200:
        return(response.content)
    else:
        return None
