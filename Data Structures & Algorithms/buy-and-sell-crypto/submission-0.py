class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        maxProfit = 0
        minimum = float("inf")
        
        for p in prices:
            if p < minimum:
                minimum = p
            
            maxProfit = max(maxProfit, p - minimum)
        return maxProfit