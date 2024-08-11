from typing import *
from collections import Counter
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        total_characters = set()

        counters = []
        for i in words:
            counters.append(Counter(i))
            total_characters |= set(i)

        answer = []
        
        for i in total_characters:
            i_occurence = float('inf')
            for j in range(len(counters)):
                i_occurence = min(counters[j][i], i_occurence)
            answer.extend([i for _ in range(i_occurence)])
        return answer

