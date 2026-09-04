class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []
        current = []
        usedNumbers = set()

        def backtrack(current):
            if len(current) == len(nums):
                results.append(current.copy())

            for i in range(len(nums)):
                if nums[i] in usedNumbers:
                    continue
                current.append(nums[i])
                usedNumbers.add(nums[i])
                backtrack(current)
                current.pop()
                usedNumbers.remove(nums[i])

        backtrack(current)
        return results

        