import asyncio
import json
import MetaTrader5 as mt5
from ap_mt5.client import TradeClient
from ap_mt5.config import assets_to_use
from ap_mt5.order_open import open_buy
import time 

def clean_prices(prices):
    return_value = {}
    for symbol in prices:
        if symbol.name in assets_to_use:
            return_value[symbol.name] = {
                "asset": symbol.name,
                "ask": symbol.ask,
                "bid": symbol.bid
            }
    return return_value

def clean_account(account):
    return {
        "account_number" : account.login,
        "balance": account.balance,
        "profit": account.profit,
        "equity": account.equity,
        "margin": account.margin,
        "currency": account.currency,
        "leverage": account.leverage
    }

async def get_prices(trade_client):
    symbols = await trade_client.get_symbols()
    return clean_prices(symbols)

async def price_checker(client):
    prices = await get_prices(client)
    while True:
        new_prices = await get_prices(client)
        for p in new_prices:
            if prices[p] != new_prices[p]:
                print("{} price changed ({} {})".format(p, new_prices[p]["bid"], new_prices[p]["ask"]))
                prices[p] = new_prices[p]

async def account(client):
    account = await client.get_account()
    print(clean_account(account))


async def open_trade(client):
   await open_buy(client,"EURUSD", 20, 10)

async def run():
    mt5.initialize()
    client = TradeClient()
    #await price_checker(client)
    #await account(client)
    await open_trade(client)
 

if __name__ == "__main__":
    asyncio.run(run())
