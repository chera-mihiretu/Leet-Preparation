from typing import *
class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        pref = [0]
        for i in range(len(arr)):
            pref.append(pref[-1] ^ arr[i])
        answer = []
        
        for fr, to in queries:
            answer.append(pref[to + 1] ^ pref[fr])
        return answer 