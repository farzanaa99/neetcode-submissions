class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        max_heap = [-num for num in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            stoneY = -heapq.heappop(max_heap)
            stoneX = -heapq.heappop(max_heap)

            if stoneY != stoneX:
                leftover = stoneY - stoneX
                heapq.heappush(max_heap, -leftover)
    
        return -max_heap[0] if max_heap else 0