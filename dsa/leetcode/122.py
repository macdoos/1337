# O(n) time | O(1) space
def maxProfit(prices):
    i = 0
    lo = 0
    hi = 0
    n = len(prices)
    profit = 0

    while i < n-1:
        while i < n-1 and prices[i] >= prices[i+1]:
            i += 1
        lo = prices[i]

        while i < n-1 and prices[i] <= prices[i+1]:
            i += 1
        hi = prices[i]
        profit += hi - lo

    return profit

prices = [7,1,5,3,6,4]
print(maxProfit(prices))
