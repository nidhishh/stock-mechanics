#this will store the bids and asks of traders
class OrderBook:
    def __init__(self):
        self.bids=[]
        self.ask= []
    #best bid is the highest bid amt
    def best_bid(self):
        return max(self.bids)
    #best ask is the lowest ask amt
    def best_ask(self):
        return min(self.ask)


