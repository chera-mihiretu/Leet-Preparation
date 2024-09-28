from typing import *

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        l_o = {c:i for i, c in enumerate(s)}
        seen = set()
        stack=[]
        for i, c in enumerate(s):
            if c not in seen:
                while stack and stack[-1] > c and i < l_o[stack[-1]]:
                    seen.discard( stack.pop())
                seen.add(c)
                stack.append(c)
        return "".join(stack)