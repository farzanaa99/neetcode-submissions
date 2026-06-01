class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        maxlength = 0
        hashset = set(nums)
        start = 0

        for i, num in enumerate(nums):
            if num - 1 not in hashset:
                start = num
                length = 0
        
                while start in hashset:
                    length += 1 
                    start += 1

                maxlength = max(maxlength, length)
        return maxlength

        