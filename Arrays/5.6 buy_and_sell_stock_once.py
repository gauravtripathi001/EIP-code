def buy_and_sell_stock_once(prices):
    min_price_so_far,max_profit=float('inf'),0.0
    for price in prices:
        max_profit_sell_today=price-min_price_so_far
        print("max_profit_sell_today",max_profit_sell_today)
        max_profit=max(max_profit,max_profit_sell_today)
        print("max_profit",max_profit)
        min_price_so_far=min(min_price_so_far,price)
        print("min_price_so_far",min_price_so_far)
        print("price",price)
    return max_profit

def test1(prices):
    min_price_so_far,max_profit=float('inf'),0.0
    for price in prices:
        min_price_so_far=min(min_price_so_far,price)
        max_profit_sell_today=price-min_price_so_far
        max_profit=max(max_profit,max_profit_sell_today)
    return max_profit
        

def main():
    prices=[310,315,275,295,260,270,290,230,255,250]
    print(test1(prices))

main()
