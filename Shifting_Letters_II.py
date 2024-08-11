from typing import *
class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        prefix = [0 for i in range(len(s) + 1)]
        for fr, to, dir in shifts:
            prefix[fr] += 1 if dir else -1
            prefix[to + 1] += -1 if dir else 1
        def to_num(char):
            return ord(char) - ord('a')
        pre = 0
        for i in range(len(prefix)):
            pre += prefix[i]
            prefix[i] = pre
        for i in range(len(s)):
            prefix[i] = (prefix[i] + to_num(s[i])) % 26
        answer = []
        for i in range(len(s)):
            answer.append(chr(ord('a') + prefix[i]))
        return ''.join(answer)
        
        
