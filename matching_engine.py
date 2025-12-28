#first we sort bids in decending and asks in ascending
def match_orders(book):
    book.bids.sort(reverse=True)
    book.ask.sort()

    #storing all trades 
    trades=[]

    #book.bid and ask contains tuples of price and qty .
    while book.bids and book.ask:
        bid_price,bid_qty=book.bids[0]
        ask_price,ask_qty=book.ask[0]
#for trade to happen the buyers should atleast match as seller price
        if bid_price >= ask_price:
            trade_qty=min(bid_qty,ask_qty)# depending upon the quantity of bid and ask the trade qty is set
            trade_price=ask_price

            trades.append((trade_price,trade_qty))#apending the trade info the trades list

            #adjusting the order book after the trade
            if bid_qty > trade_qty:
                book.bids[0]=(bid_price,bid_qty-trade_qty)
            else:
                book.bids.pop(0)
            
            if ask_qty > trade_qty:
                book.ask[0]=(ask_price,ask_qty-trade_qty)
            else:
                book.ask.pop(0)
        else:
            break
            
    return trades






