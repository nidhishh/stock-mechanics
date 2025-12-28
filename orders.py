import random
from limit_order import add_limit_order

def trader(book,mid_price):
    side=random.choice(["buy","sell"])
    price=mid_price + random.randint(-2,2)
    qty=random.randint(0,100)
    add_limit_order(book,side,price,qty)
