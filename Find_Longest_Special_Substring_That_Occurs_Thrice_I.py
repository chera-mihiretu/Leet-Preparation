from typing import *

class Solution:
    def maximumLength(self, s: str) -> int:
       
        count = defaultdict(int)
        answer = -1
        for i in range(len(s)):
            count[(s[i], 1)] += 1
            for j in range(i + 1, len(s)):
                if s[i] == s[j]:
                    count[(s[i], j - i + 1)] += 1
                else:
                    break
        # print(count)
        for (_, length), freq in count.items():
            if freq >= 3:
                answer = max(answer, length)
        return answer


                
            
