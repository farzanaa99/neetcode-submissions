class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        results = []
        current = []

        def backtrack(current, target, start):
            if target == 0:
                results.append(current.copy())
            
            if target < 0:
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                current.append(candidates[i])
                target -= candidates[i]

                backtrack(current, target, i + 1)

                current.pop()
                target += candidates[i]

        backtrack(current, target, 0)
        return results
        