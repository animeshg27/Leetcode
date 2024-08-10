prices = [1,1,0]
result = 0 
j = 0
while j != len(prices):
    for i in range(j+1,len(prices)):
        # print(f"i : {i}")
        profit = abs(prices[j] - prices[i])
        # print(f"i : {i}, profit : {profit}")
        if profit > result and prices[j] <= profit and prices[j] < prices[i]:
            result = profit
    
    j += 1 
print(result)