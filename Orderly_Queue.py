from collections import deque
from typing import * 
class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        result = list(s)
        my_min = min(result)
        answer = result.copy()
        if k == 1:
            result = deque(result)
            for i in range(len(s)):
                result.append(result.popleft())
                if result[0] == my_min:
                    comp = list(result)
                    if answer > comp:
                        answer = comp.copy()
                    print(answer, result)
                print(answer)
            return ''.join(list(answer))

        else:
            answer = list(answer)
            answer.sort()
            return ''.join(answer)
