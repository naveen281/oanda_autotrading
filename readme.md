#### To run the project install requirements.txt using:
  `pip install - r requirements.txt`
  
  and run multithread module using:
  
    `python multithread.py`
    
    
    
 ## Class TradeClient
 There are 3 main functions:
 1. For creating or getting an account id.
    In this function we initialize a constructor and passing two paramenters(accountID for getting an acoout details from oanda API,and tokens is used is used to get tokens details also from Oanda API.
   
 2. For creating or getting an transaction id and transaction details.
    In this we created an (r, variable) object which used to store details of transactions which comes from oanda API this object request to get transaction details from oanda API which is a client and transactionId"s are unique for every new transactions.
  
 3. For creating order function and getting data about the order order.
    In this order function, we passed a paramter name data then we define a variable name order_obj  which creates and order for us from getting data from accountId and tranactions details from r (already define in transaction function).
    
    
    
 ## Threading
 import threading librarry from python inbuilt library.
 Trading objects and prices comes from Oanda API(AUD_CAD,EUR_USD,USD_INR).
 
 Here, we used multithreading because if we want to trade more then one instruments at a same time in background then mmulti-thread comes in to solve this.
 1.  Define a function name of start_trading and pass a parameter name (trading_obj) and set it to run infinity until we do not stop it.
     1.1) Creates three thread here names t1,t2,t3 with the help of threading.thread in-built method.
     1.2) After that, if we want to start threads then use name of thread.start like....
          t1.start()
          t2.start()
          t3.start()
          all three methods are started.
 ## Class TradeORB(where ORB :-opening range breakout)
 There are various functions or methods we used for trading:
  1. Initialize a constructor and passed parameters name of client,instrument and sleep time. here client is itself oanda API, Instrument takes from API and sleep time is used for waiting by default its set to (600sec = 10 mins). After placing an order wheather it is sell or buy it must have to wait for given sleep time. You can change this sleep time.According to your requirements.
  
  2. Parse time function is used to parse the time in min and pass a parameter name iso_time.
     str(parser.isoparse used this inbuilt method to parse the time.
     After parsing we use some in-built methods like split function to get time in mins and second separately. so that we can use logics on them to set time from where it set its ask and bid values.
     
  3. create a function name get_rates and define a variable name x for storing insturments and its values that takes from OANDA API through passing a request to api
 
  4. creata a function name reset_high_low.
      in this function,make a empty list name of rate_bid[] and set it to true using while function ,until it breaks loop a nd get the instrument and its price and its rates and         time.
      from every 10:00 am to 10:15 am its start running and store all the values in rate_bid[] list using rate_bid.append()method. when time jump up to 10:15 then suddenly loop breaks out.
      from the rate_bid[]list we can iterate min and max value using min max in-built method.
      set min value an store it in high variable name
      set maxx value and store it lin low variable name.
  5. defined  a function name of buy, pass paramters units and its price.
  units:-number of units you want to buy.
  check its price and compare its value from min bid price its its lower than min bid price then buy given no of units otherwise wait.....
  6. defined  a function name of sell, pass paramters units and its price.
  units:-number of units you want to sell.
  check its price and compare its value from maxx bid price its its greater than min bid price then buy given no of units otherwise wait.....
  after a placing order pass it to client  create order.and wait for 10 mins.
  6 here we define a function name buy_sell_ORB
  this function is used if the high or low is none and if we want run this app at diffrent time or somehow we forgot to run it at 10 :00 am
   monitors rate of the instrument in realtime Also executes buy/sell orders based on the ORB logic and current rate and set its value in curr_time and compare its value if value is greater then the value at curr_time then it sell its unit and price at that real time and waits for 10 mins sleep time and if the value is lower then the value at curr_time then buy units at that real time rate(price) and sleep for 10 mins ,
   it repeats its process of buy sell orders unitil we do not stop this app.

   
  
      
      
  
 
          
          
     
