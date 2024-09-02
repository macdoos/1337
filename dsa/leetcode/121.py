# O(n) time | O(1) space
def maxProfit(prices):
    l, r = 0, 1
    max_profit = 0

    while r < len(prices):
        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            max_profit = max(max_profit, profit)
        else:
            l = r
        r += 1
    
    return max_profit

prices = [7,1,5,3,6,4]
print(maxProfit(prices))
