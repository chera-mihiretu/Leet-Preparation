from typing import *
from bisect import bisect_right
class Solution:
    def interestingDring(self, nums : List[int], q_s: List[int]) -> List[int]:
        answer = []
        n = len(nums)

        nums.sort()

        for i in range(len(q_s)):
            answer.append(bisect_right(nums, q_s[i]))

        return answer



if __name__ == '__main__':
    sol = Solution()
    n = int(input())
    nums = [int(i) for i in input().split()]
    q= int(input())
    q_s = []
    for i in range(q):
        q_s.append(int(input()))
    answer = sol.interestingDring(nums, q_s)

    print(*answer, sep='\n')
