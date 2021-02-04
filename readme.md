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
    
    
  ## class TradeORB (ORB :-opening range breakout)

 There are various functions or methods we used for trading:
  1. Initialize a constructor and passed parameters name of client,instrument and sleep time. here client is itself oanda API, Instrument takes from API and sleep time is used for waiting by default its set to (600sec = 10 mins). After placing an order wheather it is sell or buy it must have to wait for given sleep time. You can change this sleep time.According to your requirements.
  
  2. Parse time function is used to parse the time in min and pass a parameter name iso_time.
     str(parser.isoparse used this inbuilt method to parse the time.
     After parsing we use some in-built methods like split function to get time in mins and second separately. so that we can use logics on them to set time from where it set its ask and bid values.
     
  3. create a function name get_rates and define a variable name x for storing insturments and its values that takes from OANDA API through passing a request to api
 
  4. creata a method named `reset_high_low`
      In this method, initialised an empty list named rate_bid[], and started with a infinite while using while function with break condition, until it breaks loop(after minute>=14), get the instrument and its price and its rates and append into rate_bid.
      
      From every 10:00 am to 10:15 am its start running and store all the values in rate_bid[] list using rate_bid.append()method. when time jump up to 10:15 then loop breaks out.
      from the rate_bid[]list we can find min and max value using min max in-built method.
      - set min value to low-thresh attribute
      - set max value to high_thresh attribute
  5. Defined method named `buy`, required paramters: units and its price.
  - units:- number of units you want to buy.
  - check its price and compare its value from min bid price its its lower than min bid price then buy given no of units otherwise wait.....
  6. Defined method named sell, required paramters: units and its price.
  - units:-number of units you want to sell.
  - check its price and compare its value with max bid price is greater than min bid price then buy given no of units otherwise wait.....
  for placing order, send the order object to `create order` method.
  6 And finally method `buy_sell_ORB`:
  
  This method is responsible for:
  - resetting the ORB(Min and Max thresholds) price at 10:AM Everyday and resume trading afterward by comparing the threshold with current price by calling `reset_high_low`.
  - Keep checking prices at an interval of 1 second and store the price as current price
  - buy or sell based on current price by comparing with High/Low thresh and call `buy` / `sell` methods defined above.
  - Sleep for 10 minutes(600 secs) if successfully placed a order else 1 second.
 

  
  We will run the buy_sell_ORB method infinitely using while loop with True Condition in another function created in multithreading module
  
  

 ## Threading for concurrent trading of 3 instruments:
 used threading library from python.
 Created 3 Trading objects(AUD_CAD,EUR_USD,USD_INR) by instatiating TradeORB class.

 Here, we used multithreading because we want to trade more then one instruments concurrently in background.
 1.  Defined a function named start_trading and pass a parameter name (trading_obj) and set it to run infinity until we do not stop it.
     1.1) Creates three thread here names t1,t2,t3 with the help of threading.thread in-built method.
     1.2) After that, if we want to start threads then use name of thread.start like....
          t1.start()
          t2.start()
          t3.start()
      all three methods are started.
  
      
      
  
 
          
          
     
