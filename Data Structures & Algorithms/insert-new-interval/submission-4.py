class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        result = []
        inserted = False
      #  intervals.append(newInterval)
       # intervals.sort()

#before
        for interval in intervals:
            if interval[1] < newInterval[0]:
                result.append(interval)

#after
            elif interval[0] > newInterval[1]:
                if not inserted:
                    result.append(newInterval)
                    inserted = True
                result.append(interval)
#overlap
            else:
                newStart = min(interval[0], newInterval[0])
                newEnd = max(interval[1], newInterval[1])
                newInterval = [newStart, newEnd]

        if not inserted:
            result.append(newInterval)

        return result




        