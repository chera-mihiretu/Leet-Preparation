from typing import *

class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        hash_s = set(banned)
        answer = 0
        count = 0
        for i in range(1, n + 1):
            if i not in hash_s:
                answer += i
                if answer > maxSum:
                    return count
                count += 1
        return count
