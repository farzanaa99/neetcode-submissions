class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        overlap = 0
        prev = intervals[0][1]
        
        for interval in intervals[1:]:
            if interval[0] < prev:
                overlap += 1

            else:
                prev = interval[1]

        return overlap


        