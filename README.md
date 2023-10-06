# MT5 Trader 

First establish a connection to your mt5 no additional info will be needed. Using the function run() will initialize the connection. The **config.py** currenly has a list called asset where you can change the symbols that you want to trade within your stragety. Also the **config.py** file does have a pip_value so you don't have to calculate the pip value for every currency pair but it needs more work on it just because it only show 0.0001 so far. So if you wanted to trade JPY pairs or commodity pairs.

# Client 
The **client.py** has a class called TradeClient and it has a few function so far. Firstly, the get symbols function will get all the symbols you are allowed to trade within your broker. secondly, the get account gets your current account details and the **model.py** show you how the data will be model once you called this function. 


until the next time!!! Will update the README the more i continue to work on this project 