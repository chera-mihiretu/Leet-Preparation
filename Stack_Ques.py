from typing import *
from collections import deque
from sys import stdin,stdout
# take input
input = lambda: stdin.readline().strip()
# solution
def solution():
    n = int(input())
    array = [int(i) for i in input().split()]
    que = deque()
    for i in range(n):
        if i & 1:
            # odd
            que.append(array[i])
        else:
            que.appendleft(array[i])
    answer = []
    while que:
        answer.append(que.popleft())
    print(*answer)

# run the code
if __name__ == '__main__':
    test_case = 1 #int(input())
    for i in range(test_case):
        solution()