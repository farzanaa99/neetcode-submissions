class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = float("inf")
        maxProfit = float("-inf")

        for p in prices:
            if p < lowest:
                lowest = p

            maxProfit = max(maxProfit, p - lowest)

        return maxProfit
