class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = 0
        curr = 0
        profit = 0
        while(curr < len(prices)):
            if(prices[curr] > prices[sell]):
                sell = curr
                profit = max(profit, prices[sell] - prices[buy])
            if(prices[curr] < prices[buy]):
                buy = curr
                sell = curr
            curr += 1
        return profit