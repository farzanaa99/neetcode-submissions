class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        results = []
        current = []
        def backtrack(current, nums, start):
            results.append(current.copy())
            for i in range(start, len(nums)):
                current.append(nums[i]) #add num
                backtrack(current, nums, i + 1) #backtrack
                current.pop()


        backtrack(current, nums, 0)
    
        return results
