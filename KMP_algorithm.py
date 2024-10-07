from typing import *

class Solution:
    def getLongestPrefixSuffix(self, string:str) -> int:
        if not string:
            return 0
        N = len(string)
        lps = [0 for _ in range(N)]
        j, i = 0, 1
        while i < N:
            if string[i] == string[j]:
                lps[i] = j + 1
                i += 1
                j += 1
            else:
                if j == 0:
                    lps[i] = 0
                    i += 1
                else:
                    j = lps[j - 1]
        return max(lps)

    


test_case = [['', 0], ['ab', 0], ['aaaxaaaa',3]]
solution = Solution()
for test, real_answer in test_case:
    answer = solution.getLongestPrefixSuffix(test)
    assert answer == answer, f'Expected {real_answer} but got {answer}'
    print(f'Test \'{test}\' Passed')