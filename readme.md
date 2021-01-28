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
          
          
     
