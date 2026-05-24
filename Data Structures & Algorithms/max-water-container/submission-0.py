class Solution:
    def maxArea(self, heights: List[int]) -> int:

        start = 0
        end = len(heights) - 1
        maxArea = 0

        while start < end:
            if heights[start] < heights[end]:
                maxArea = max(maxArea, heights[start] * (end-start))
                start+=1

            else:
                maxArea = max(maxArea, heights[end] * (end-start))
                end-=1

        return maxArea

        