from typing import *

from heapq import *

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        for i in matrix:
            heap.extend(i)
        heapify(heap)
        number = heap[0]
        for i in range(k):
            number = heappop(heap)
        return number