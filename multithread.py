# importing custom class
from trade_client import TradeClient
from trading import TradeORB

# importing threading  library
import threading

accountID = '101-001-17725626-001'
token = '6ee3a98b16114fb7671586deb515ff6e-dfa1d182025c98ea8887e2ac1f7d4ec2'

# creating oanda client object
trade_client = TradeClient(accountID, token)
print(trade_client.get_accountID())
print(trade_client.get_transaction_details('8'))


# EURO USD trading object
trade_EUR_USD = TradeORB(trade_client, "EUR_USD")
print("Current EUR_USD bid rate: ",trade_EUR_USD.get_rates()['prices'][0])

# AUS CAD (Australian Dollar-Canadian Dollar) trading object
trade_AUD_CAD = TradeORB(trade_client, "AUD_CAD")
print("Current AUD_CAD bid rate: ",trade_AUD_CAD.get_rates()['prices'][0])

# USD INR trading object
trade_USD_INR = TradeORB(trade_client, "USD_INR")
print("Current USD_INR bid rate: ",trade_USD_INR.get_rates()['prices'][0])


def start_trading(trading_obj):
    # infinite loop over buy sell method
    while True:
        trading_obj.buy_sell_ORB()


if __name__ == '__main__':
    # creating thread for each object type
    t1 = threading.Thread(target=start_trading, args=(trade_EUR_USD,))
    t2 = threading.Thread(target=start_trading, args=(trade_AUD_CAD,))
    t3 = threading.Thread(target=start_trading, args=(trade_USD_INR,))

    # starting thread 1
    t1.start()
    # starting thread 2
    t2.start()
    # starting thread 3
    t3.start()

    # if threads completely executed
    print("Done!")






