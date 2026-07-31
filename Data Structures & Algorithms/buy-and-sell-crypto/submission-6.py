class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #2 pointer approach

        buy = prices[0]

        max = 0;

        for i in prices:
            if buy > i:
                buy = i
            
            if i - buy > max:
                max = i - buy
        
        return max
