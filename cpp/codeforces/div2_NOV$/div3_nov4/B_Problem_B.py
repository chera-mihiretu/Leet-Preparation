from sys import stdin,stdout
# take input
input = lambda: stdin.readline().strip()
# solution
def solution():
    n = int(input())
    nums = [int(i) for i in input().split()]

    ones = nums.count(1)
    answer = 0

    for i in range(len(nums) - 1, -1, -1):
        if ones == 0:
            break
        if nums[i] == 0:
            answer += 1
            nums[i] = 1
        ones -= nums[i]
    print(answer)

# run the code
if __name__ == '__main__':
    test_case = int(input())
    for i in range(test_case):
        solution()