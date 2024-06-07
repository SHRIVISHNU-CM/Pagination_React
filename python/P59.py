def MaxProfit(prices):
    max_pro = 0
    for i in range(len(prices)):
        for j in range(i+1 , len(prices)):
            profit = prices[j] - prices[i]

            if profit > 0:
                max_pro = max(max_pro , profit)
    
    return max_pro

arr = [7,1,5,3,6,4]

res  = MaxProfit(arr)
print(res)