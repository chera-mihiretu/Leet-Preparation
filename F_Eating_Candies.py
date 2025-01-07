from sys import stdin,stdout
# take input
input = lambda: stdin.readline().strip()
# solution
def solution():
    n = int(input())
    nums = [int(i) for i in input().split()]
    alice = 0
    bob = len(nums)-1
    sum_alice = 0
    sum_bob = 0
    result = 0
    while(alice < bob):

        sum_alice += nums[alice]
        sum_bob += nums[bob]

        if sum_alice == sum_bob:
            result = (alice+1) + (len(nums)-bob)
            alice += 1
            bob -= 1
        elif sum_alice > sum_bob:
            sum_alice -= nums[alice]
            bob -= 1
        else:
            sum_bob -= nums[bob]
            alice += 1
    return result

# run the code
if __name__ == '__main__':
    test_case = int(input())
    for i in range(test_case):
        print(solution())