from typing import *
from collections import Counter
class Solution():
    def splitString(self, s:str) -> int:
        count_right = Counter(s)
        count_left = Counter()
        answer = 0
        for i in s:
            count_right[i] -= 1
            if count_right[i] == 0:
                count_right.pop(i)
            count_left[i] += 1

            if len(count_left) == len(count_right):
                answer += 1
        return answer
    

