from typing import *

class Solution:
    def minEnd(self, n: int, x: int) -> int:
        steps = n - 1
        result = x
        start = 0
        while steps:
            while (1 << start) & result:
                start += 1
            move = steps & 1
            steps >>= 1
            result |= (move << start)
            start += 1
        return result
            
            

            