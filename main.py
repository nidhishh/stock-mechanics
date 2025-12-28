from orderbook import OrderBook
from orders import trader
from matching_engine import match_orders

price=[]
book=OrderBook()
mid_price=100

for t in range(100):
    trader(book,mid_price)

    trades = match_orders(book)
#idk why did we do this
    if trades:
        mid_price= trades[-1][0]
        price.append(mid_price)

print(price)