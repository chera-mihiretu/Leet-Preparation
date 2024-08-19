from typing import *

class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        def backtrack(a_s, copy):
            if a_s == n:
                return 0
            if a_s > n:
                return float('inf')
            right = backtrack(a_s + copy, copy)
            left = backtrack(a_s * 2, a_s) 
            return min(left + 2, right + 1)
        return backtrack(1, 1) + 1