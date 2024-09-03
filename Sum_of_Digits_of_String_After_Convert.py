from typing import *

class Solution:
    def getLucky(self, s: str, k: int) -> int:
        total = []
        for i in s:
            total.append(str(ord(i) - ord('a') + 1))
        total = ''.join(total)
        current = total
        for i in range(k):
            total = str(current)
            
            current = 0
            for i in total:
                current += int(i)
        return current
