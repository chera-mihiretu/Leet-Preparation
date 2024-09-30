from typing import *

def solution(nums):
    N = len(nums)
    M = len(nums[0])
    answer = [[0 for _ in range(M)] for __ in range(N)]
    for i in range(N):

        for j in range(M):
            if i + 1 < N:
                answer[i + 1][j] -= nums[i][j]
            if j + 1 < M:
                answer[i][j + 1] -= nums[i][j]
            if i + 1 < N and j + 1 < M:
                answer[i + 1][j + 1] += nums[i][j]
    for i in range(N):

        for j in range(M):
            answer[i][j] += nums[i][j]
    return answer

nums1 = [[1,2], [3,4]]

answer = [[1,1],[2,0]] 
canAnswer = solution(nums1)
assert canAnswer == answer, f'{canAnswer} was expected but {nums1} was returned'  

                       