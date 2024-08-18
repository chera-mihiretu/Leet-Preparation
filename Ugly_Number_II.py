from typing import *
from heapq import *
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        count = 0
        heap = [1] 
        seen = set([1])
        answer = 1
        while count < n:
            #print(answer)
            answer = heappop(heap)
            count += 1
            for i in [2,3,5]:
                if answer * i not in seen:
                    seen.add(answer * i)
                    heappush(heap, answer * i)
        return answer
            

