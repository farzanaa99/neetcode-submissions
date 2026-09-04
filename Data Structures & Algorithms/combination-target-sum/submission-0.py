class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        results = []
        current = []

        def backtrack(current, target, start):
            if target == 0:
                results.append(current.copy())

            if target < 0:
                return

            for i in range(start, len(nums)):
                current.append(nums[i])
                target -= nums[i]
                backtrack(current, target, i)
                target += nums[i]
                current.pop()

        backtrack(current, target, 0)
        return results

        