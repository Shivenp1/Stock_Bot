from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce
from alpaca.data.historical import StockHistoricalDataClient
from alpaca.data.requests import StockBarsRequest
from alpaca.data.timeframe import TimeFrame
from datetime import datetime, timedelta

# Set up the client and the stock data

client = TradingClient("PK8J0Z1YWJQ53DWBOW2S", "mzwRDXyGC6v5U9AUFaBschWmWJOx0Rx2rbhQKF9G")
data_client = StockHistoricalDataClient("PK8J0Z1YWJQ53DWBOW2S", "mzwRDXyGC6v5U9AUFaBschWmWJOx0Rx2rbhQKF9G")



# Get the stock parameters for the stock that you want to trade 


end_date = datetime.now().date()
start_date = (datetime.now().date() - timedelta(days=365))

request_params = StockBarsRequest(
    symbol_or_symbols="SPY",
    timeframe=TimeFrame.Day,
    start=start_date,
    end=end_date
)

bars = data_client.get_stock_bars(request_params)

close_prices = [bar.close for bar in bars['SPY']]

#Function to calculate the Moving Averages

def calculate_moving_average(prices, window):
    if len(prices) < window:
        return None
    return sum(prices[-window:]) / window


ma_50 = calculate_moving_average(close_prices, 50)
ma_200 = calculate_moving_average(close_prices, 200)

# Buy the stock if the Moving Average fits Golden Cross Criteria
if ma_50 and ma_200 and ma_50 > ma_200:
    market_order_data = MarketOrderRequest(
        symbol="SPY",
        qty=10,
        side=OrderSide.BUY,
        time_in_force=TimeInForce.DAY
    )
    client.submit_order(market_order_data)

