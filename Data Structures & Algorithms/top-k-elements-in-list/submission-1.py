class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counts = Counter(nums)

        heap = []

        for num, freq in counts.items():
            heapq.heappush(heap, (-freq, num))

        answer = []
        for _ in range(k):
            freq, num = heapq.heappop(heap)
            answer.append(num)

        return answer