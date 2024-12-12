from typing import *
from heapq import *
from math import sqrt, floor
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heap = [-i for i in gifts]
       
        heapify(heap)
        while k:
            top = -heappop(heap)
            heappush(heap, -floor(sqrt(top))) 
            k -= 1
        return -sum(heap)