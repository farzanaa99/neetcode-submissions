class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        maxSum = float("-inf")
        sum = 0

        for num in nums:
            sum = max(num, sum + num)
            maxSum = max (maxSum, sum)

        return maxSum

        