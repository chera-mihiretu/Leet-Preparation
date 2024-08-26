from sys import stdin,stdout
from collections import Counter
# take input
input = lambda: stdin.readline().strip()
# solution
def solution():
    n = int(input())
    nums = [int(i) for i in input().split()]
    count = Counter(nums)

    mx = 0
    for i in count:
        mx = max(count[i], mx)
    print(len(nums) - mx )




    

# run the code
if __name__ == '__main__':
    test_case = int(input())
    for i in range(test_case):
        solution()