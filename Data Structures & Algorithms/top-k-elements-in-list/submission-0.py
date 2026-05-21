class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counts = Counter(nums)
        heap = [(-freq, num) for num, freq in counts.items()]
        heapq.heapify(heap)
        
        result = []

        for _ in range(k):
            freq, num = heapq.heappop(heap)
            result.append(num)

        return result

        