class TimeMap:

    def __init__(self):
        self.hashmap = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hashmap:
            self.hashmap[key] = []
        self.hashmap[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hashmap:
            return ""

        arr = self.hashmap[key]

        start = 0
        end = len(arr) - 1
        res = ""

        while start <= end:
            mid = (start+end) // 2
            if arr[mid][0] <= timestamp:
                res = arr[mid][1]
                start = mid + 1
            else:
                end = mid - 1

        return res



        
