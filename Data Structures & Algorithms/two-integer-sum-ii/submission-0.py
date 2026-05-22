class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        start = 0
        end = len(numbers) - 1
        result = []

        while start < end:
            add = numbers[start] + numbers[end]
            if add < target:
                start+=1

            elif add > target:
                end-=1
            
            else:
                return [start+1, end+1]


        