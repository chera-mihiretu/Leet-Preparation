from typing import *
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        list_of_words = s1.split() + s2.split()

        count = Counter(list_of_words)
        answer = []
        for i in count:
            if count[i] == 1:
                answer.append(i)
        return answer