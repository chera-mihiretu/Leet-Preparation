from typing import *

def solution():
    n = int(input())
    nums = [int(i) for i in input().split()]
    def dp(index, number,  count):
        if count == 0:
            return 1
        if index == n:
            return 0
        pick = 0
        if nums[index] < number:
            pick =  dp(index + 1, nums[index], count - 1) 
        not_pick = dp(index + 1, number, count)
        return pick + not_pick
    
    return dp(0, float('inf'), 3)

if __name__ == '__main__':
    print(solution())   