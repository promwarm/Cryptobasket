import Scraper
import json
import time
import datetime
import pytz

debug = True

# Asks input from user (1 coin at the time)
def ask_coins():
    if debug: print ('*** DEBUG *** ask_coins()')
    coins = input('Enter a coin symbol: ')
    return coins

# Checks if user input is a valid coin
def check_coins(coins):
    if debug: print('*** DEBUG *** check_coins() with parameter '+coins)
    if debug: print('*** DEBUG *** You want to check {0}'.format(coins))
    j = json.loads(Scraper.scrape(coins,'BTC,USD'))
    if 'Response' in j:
        print ("Could not find coin! - "+j['Message'])
        return False
    else:
        if debug: print ("*** DEBUG *** Your coin {0} exists, currently costs {1} BTC, which is the equivalent of ${2}".format(coins,j['BTC'],j['USD']))
        return True

def parse_coin(coin):
    if debug: print ('*** DEBUG *** parse_coins() with parameter '+coin)
    coin = coin.upper()
    valid_coin = check_coins(coin)
    if debug: print ('*** DEBUG *** Is coin valid? '+str(valid_coin))
    if valid_coin:
        j = json.loads(Scraper.scrape(coin,'BTC,USD')) # TODO I'll scrape twice this way, I want the check_coins ideally to return the json earlier created
        price_btc = j['BTC']
        price_usd = j['USD']
        dt_utcnow = datetime.datetime.now(tz=pytz.UTC)
        price_dt = dt_utcnow
        #dt_amsterdam = dt_utcnow.astimezone(pytz.timezone('Europe/Amsterdam'))
        print('Current price in BTC: {:1.8f}'.format(price_btc))
        print('Current price in USD: {:5.4f}'.format(price_usd))
        jsonData = '{"ticker": "{'+coin+'}", "price_btc": "'+str(price_btc)+'", "price_usd": "'+str(price_usd)+'", "datetime": "{'+str(price_dt)+'}"}'
        jsonToPython = json.loads(jsonData)
        if debug: print('*** DEBUG *** Fetched by Cryptobasket at ' + str(price_dt))
        return jsonToPython

def save_coins():
    if debug: print ('*** DEBUG *** save_coins()')