from sys import stdin,stdout
from math import ceil
# take input
input = lambda: stdin.readline().strip()
# solution
def solution():
    n = int(input())
    nums = [int(i) for i in input().split()]
    nums.sort()
    answer = 0
    for i in range(len(nums)//2):
        answer += abs(nums[i] - nums[ceil(len(nums) /2) + i])
    print(answer)
        
# run the code
if __name__ == '__main__':
    test_case = int(input())
    for i in range(test_case):
        solution()