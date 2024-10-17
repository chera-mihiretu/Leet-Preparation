from typing import *

class Solution:
    def maximumSwap(self, num: int) -> int:
        num_sep = []
        answer = 0
        while num:
            rem = num % 10
            num = num // 10
            num_sep.append(rem)
        for i in range(len(num_sep) - 1, -1, -1):
            for j in range(i - 1, -1, -1):
                if num_sep[j] > num_sep[i]:
                    num_sep[i], num_sep[j] = num_sep[j], num_sep[i]
                    break
            for i in range(len(num_sep)):
                answer += num_sep[i] * (i + 1)
            return answer