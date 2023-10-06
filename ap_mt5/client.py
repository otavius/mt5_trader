import asyncio
import concurrent.futures
import MetaTrader5 as mt5

class TradeClient:
    def __init__(self, loop=None):
        self.loop = loop or asyncio.get_running_loop()
        self.pool = concurrent.futures.ThreadPoolExecutor()

    async def get_symbols(self):
        return await self.loop.run_in_executor(self.pool, lambda: mt5.symbols_get())
    
    async def get_account(self):
        return await self.loop.run_in_executor(self.pool,lambda:mt5.account_info())
    
    async def get_symbol(self, symbol_name):
        return await self.loop.run_in_executor(self.pool,lambda:mt5.symbol_info(symbol_name))
    
    async def order_send(self, request):
        return await self.loop.run_in_executor(self.pool,lambda:mt5.order_send(request))