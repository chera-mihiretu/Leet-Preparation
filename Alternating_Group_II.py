from typing import *
class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        answer = 0
        start = 0
        for i in range(1, len(colors) + k - 1):
            if colors[(i) % len(colors)] == colors[(i-1) % len(colors)]:
                start = i
            if (i - start + 1) > k:
                start += 1
            if i - start + 1 == k:
                answer += 1
        return answer