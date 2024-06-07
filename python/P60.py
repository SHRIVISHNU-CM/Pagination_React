def max_profit(prices):
    min_price = float('inf')
    max_pro = 0

    for price in prices:
        if price < min_price:
            min_price = price

        profit = price - min_price
        
        if profit > max_pro:
            max_pro = profit
    return max_pro

arr =  [7,1,5,3,6,4]
res  = max_profit(arr)
print(res)