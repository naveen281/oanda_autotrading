import oandapyV20
import oandapyV20.endpoints.pricing as pricing

# importing inbuilt libraries
from dateutil import parser
import time


class TradeORB:
    def __init__(self, client, instrument, order_sleep_time = 600):
        self.__client = client
        self.__instrument = instrument
        self.__low = None
        self.__high = None
        self.__order_sleep_time = order_sleep_time

    def get_instrument(self):
        return self.__instrument

    def parse_time(self, ISO_time):
        """
        To Parse DateTime in UTC format from ISO Format
        """
        return str(parser.isoparse(ISO_time)).split()[1].split(':')
    
    
    def return_ask_bid(self, price_response):
        """
        returns asking and bidding price from a response object
        """

        # ask = price_response['prices'][0]['closeoutAsk']
        bid = price_response['prices'][0]['closeoutBid']
        return bid

    def get_rates(self):
        """
        return latest rate of the instrument
        """
        params = {"instruments": self.__instrument}
        x = (pricing.PricingInfo(self.__client.get_accountID(), params=params))
        return self.__client.get_clientAPI().request(x)

    def reset_high_low(self):
        """
        resets the high and low(ORB) everyday by monitoring max and min values
        between 10:00 AM and 10:15 AM.
        """
        # rate_ask = []
        rate_bid = []
        while True:
            price_response = self.get_rates()
            ISO_time = price_response['time']
            time = self.parse_time(ISO_time)

            # ask, bid = self.return_ask_bid(price_response)
            bid = self.return_ask_bid(price_response)

            # rate_ask.append(ask)
            rate_bid.append(bid)

            # if time crosses 10:15AM breaking the loop
            if int(time[1]) >= 15:
                break

            # 1 second Sleep before updating
            time.sleep(1)

        # select max of the 15 min window
        print("Max Window")
        self.__high = max(rate_bid)
        self.__low = min(rate_bid)
        return

    def buy(self, price, units="5"):
        """
        exectues a buying order
        """
        print("buying:")
        instrument = self.__instrument

        data = {
            "order": {
                "price": "1.2",
                "stopLossOnFill": {
                    "timeInForce": "GTC",
                    "price": price
                },
                "timeInForce": "GTC",
                "instrument": instrument,
                "units": units,
                "type": "LIMIT",
                "positionFill": "DEFAULT"
            }
        }

        resp = self.__client.create_order(data)
        print(resp)

    def sell(self, price, units="-5"):
        print("Selling: ")
        instrument = self.__instrument

        data = {
            "order": {
                "price": "1.2",
                "stopLossOnFill": {
                    "timeInForce": "GTC",
                    "price": price
                },
                "timeInForce": "GTC",
                "instrument": instrument,
                "units": units,
                "type": "LIMIT",
                "positionFill": "DEFAULT"
            }
        }

        resp = self.__client.create_order(data)
        print(resp)


    def buy_sell_ORB(self):
        """
        Infinite loop to:
        Executes the ORB logic to setup prices using reset_high_low method
        and monitors rate of the instrument in realtime.
        Also executes buy/sell orders based on the ORB logic and current rate
        """

        price_response = self.get_rates()
        ISO_time = price_response['time']

        # if support and resistance are None, setting it to current Value to intialise
        if self.__high is None and self.__low is None:
            self.__high = self.return_ask_bid(price_response)
            self.__low = self.return_ask_bid(price_response)

        # Parsing time to UTC format from ISO Format
        cur_time = self.parse_time(ISO_time)

        # reset support and resistance at 10:00 AM
        if int(cur_time[0]) == 10 and int(cur_time[1]) < 15:
            self.reset_high_low()

        # getting current bidding price
        cur_bid_price = self.return_ask_bid(price_response)

        # placing order based current bid price
        # buying order
        if self.__high < cur_bid_price:
            print("Buying at: ", cur_bid_price)
            self.buy(cur_bid_price)

            # sleep for 10 minutes i.e 600 Seconds after placing order
            time.sleep(self.__order_sleep_time)

        # selling condition
        if self.__low > cur_bid_price:
            print("Selling at: ", cur_bid_price)
            self.sell(cur_bid_price)

            # sleep for 10 minutes i.e 600 Seconds after placing order
            time.sleep(self.__order_sleep_time)

        # sleep for one second after checking current price
        time.sleep(1)

        print(self.__high)
        print(self.__low)
