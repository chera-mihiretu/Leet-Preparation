from sys import stdin,stdout
# take input
input = lambda: stdin.readline().strip()
# solution
def solution():
    n,s = [int(i) for i in input().split()]
    nums = [int(i) for i in input().split()]
    total = 0
    answer = 0
    start = 0
    for i in range(n):
        total += nums[i]
        while total < s:
            total -= nums[start]
            start += 1
        answer = max(answer, i - start +1)
    print(answer)


# run the code
if __name__ == '__main__':
    test_case = 1 #int(input())
    for i in range(test_case):
        solution()