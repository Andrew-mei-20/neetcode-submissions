class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        
        max = 0
        for i in prices:
            if i < buy:
                buy = i
            
            if(i - buy > max):
                max = i - buy
            

        return max