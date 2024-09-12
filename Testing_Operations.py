# Access the Users Information and connect to the API

from alpaca.trading.client import TradingClient 
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce, QueryOrderStatus
from alpaca.trading.requests import LimitOrderRequest
from alpaca.trading.requests import GetOrdersRequest
from alpaca.data.live import StockDataStream


client = TradingClient("PK8J0Z1YWJQ53DWBOW2S", "mzwRDXyGC6v5U9AUFaBschWmWJOx0Rx2rbhQKF9G")
'''

# Create a market order
market_order_data = MarketOrderRequest(
    symbol="SPY", 
    qty=10, 
    side=OrderSide.BUY,
    time_in_force=TimeInForce.DAY
)

market_order = client.submit_order(market_order_data)

print(market_order)

# Creates a limit order 

limit_order_data = LimitOrderRequest(
        symbol = "SPY",
        qty = 10, 
        side = OrderSide.BUY,
        time_in_force = TimeInForce.Day,
        limit_price = 550.00)

limit_order = client.submit_order(limit_order_data)

print(limit_order)



# Getting Order Status

parameters = GetOrdersRequest(
    status=QueryOrderStatus.OPEN,
)

orders = client.get_orders(parameters)
print(orders)



# check the positions that you are in

positions = client.get_all_positions()

print(positions)

for position in positions:
    print(position.symbol, position.current_price)

    # Stream the Data

stream = StockDataStream("PK8J0Z1YWJQ53DWBOW2S", "mzwRDXyGC6v5U9AUFaBschWmWJOx0Rx2rbhQKF9G")

async def handle_trade(data):
    print(data)

stream.subscribe_trades(handle_trade, "AAPl")

stream.run()

'''