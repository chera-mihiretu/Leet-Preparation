from typing import *
class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        answer = start ^ goal
        count = 0
        while answer:
            count += answer & 1
            answer = answer >> 1
        return count