class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = []
        current = []
        def backtrack(current, start):
            results.append(current.copy())

            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue

                current.append(nums[i])
                backtrack(current, i+1)
                current.pop()

        backtrack(current, 0)
        return results