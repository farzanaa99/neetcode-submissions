class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        sums = set()

        for i in range(len(nums)-2):

            left = i + 1
            right = len(nums) - 1

            if i > 0 and nums[i] == nums[i-1]:
                continue;

            while left < right:
                added = nums[i] + nums[left] + nums[right]
                
                if added == 0:
                    sums.add((nums[i], nums[left], nums[right]))
                    right-=1
                    left+=1

                elif added > 0:
                    right-=1
                    
                else:
                    left+=1
        
        return list(sums)

        