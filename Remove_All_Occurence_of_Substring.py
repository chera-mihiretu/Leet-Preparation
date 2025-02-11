from typing import *
class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        res = []
        part = list(part)
        pn = len(part)
        
        for ch in s:
            res.append(ch)
            if len(res) >= pn and res[-pn:] == part:
                res = res[:-pn]

        return "".join(res)    