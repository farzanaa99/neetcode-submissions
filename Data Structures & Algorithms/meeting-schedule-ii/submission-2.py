"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x:x.start)
        startArray = []
        endArray = []
        room = 0
        maxRooms = 0

        for interval in intervals:
            startArray.append(interval.start)
            endArray.append(interval.end)

        startArray.sort()
        endArray.sort()

        s = 0
        e = 0
        while s < len(startArray) and e < len(endArray):
            if startArray[s] < endArray[e]:
                s+=1
                room += 1
                maxRooms = max(room, maxRooms)
            elif startArray[s] >= endArray[e]:
                e += 1
                room -= 1
            
        return maxRooms
        