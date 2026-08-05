class Solution:
    def stocks(self,prices):
        # maximum = 0
        # n = len(prices)

        # for i in range(n):
        #     for j in range(i+1,n):
        #         profit = prices[j] -prices[i]
        #         maximum = max(maximum,profit)
        
        # return profit

        minimum = prices[0]
        profit = 0

        for price in prices:
            minimum = min(minimum,price)
            current_price = price - minimum
            profit = max(current_price,profit)
        return profit
sol = Solution()
print(sol.stocks([5,2,0,1]))
print(sol.stocks([7,1,5,3,6,4]))