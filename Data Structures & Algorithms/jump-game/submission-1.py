class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maximumJump = 0

        for i in range(len(nums)):
            if i > maximumJump:
                return False
            maximumJump = max(maximumJump, i + nums[i])

        return True
        