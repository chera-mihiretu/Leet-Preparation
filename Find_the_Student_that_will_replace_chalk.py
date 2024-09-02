from typing import *
class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        total = sum(chalk)
        left = k % total 
        for i in range(len(chalk)):
            if left - chalk[i] < 0:
                return i
            left -= chalk[i]
        