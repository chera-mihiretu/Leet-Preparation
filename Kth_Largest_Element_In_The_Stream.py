from typing import *
from heapq import *
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = nums
        heapify(nums)
        self.max = k
        while len(self.heap) > self.max:
            heappop(self.heap)

    def add(self, val: int) -> int:

        heappush(self.heap, val)
        if len(self.heap) > self.max:
            heappop(self.heap)
        return self.heap[0]