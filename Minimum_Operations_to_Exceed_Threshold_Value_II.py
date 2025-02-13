from typing import *

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heap = nums[::]
        step = 0
        heapify(heap)
        while heap[0] < k and len(heap) > 1:
            step += 1
            first = heappop(heap)
            second = heappop(heap)

            heappush(heap, min(first, second) * 2 + max(first, second))
    
        return step
        