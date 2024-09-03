from typing import *
from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = Counter()
        answer = 0
        start= 0
        for i in range(len(s)):
            count[s[i]] += 1
            if (i - start + 1) - max(count.values()) > k:
                count[s[start]] -= 1
                start += 1
            
            answer = max(answer, i - start + 1)
           
        return answer

             